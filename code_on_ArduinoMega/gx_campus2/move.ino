/* 这里存储一些和底盘运动控制有关的函数 */
#include "gx_campus2.h"

// 创建4个编码器对象
Encoder ENC[4] = {
    Encoder(ENCODER_A, DIRECTION_A), Encoder(ENCODER_B, DIRECTION_B),
    Encoder(ENCODER_C, DIRECTION_C), Encoder(ENCODER_D, DIRECTION_D)};
long newPulses[4] = {0, 0, 0, 0};         // 四个车轮的定时中断编码器四倍频速度

// 编码器PID参数
float targetPulses[4] = {0, 0, 0, 0};     // 用于控制电机的目标脉冲数
float feedbackVel[4] = {0, 0, 0, 0};
double outPWM[4] = {0, 0, 0, 0};
// 创建4个速度PID控制对象
/*PID(float min_val, float max_val, float kp, float ki, float kd)
 * float min_val = min output PID value
 * float max_val = max output PID value
 * float kp = PID - P constant PID控制的比例、积分、微分系数
 * float ki = PID - I constant
 * float di = PID - D constant
 * Input	(double)输入参数feedbackVel，待控制的量
 * Output	(double)输出参数outPWM，指经过PID控制系统的输出量
 * Setpoint	(double)目标值targetVel，希望达到的数值
 */
PID VeloPID[4] = { PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd), PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd),
                   PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd), PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd)};

// 陀螺仪PID参数
float newYawPulses = 0;         // 四个车轮的定时中断编码器四倍频速度
float targetYawPulses = 0;      // 用于控制车身的目标朝向角
float feedbackYawVel = 0;
double outYawPWM = 0;
double outYawPWM_old = 0;
// 创建1个陀螺仪速度PID控制对象
PID YawPID = PID(PWM_MIN, PWM_MAX, Kp_yaw, Ki_yaw, Kd_yaw);

// 七路PID参数
float newSevenPulses = 0;         // 四个车轮的定时中断编码器四倍频速度
float targetSevenPulses = 0;      // 用于控制车身的目标朝向角
float feedbackSevenVel = 0;
double outSevenPWM = 0;
double outSevenPWM_old = 0;
// 创建1个陀螺仪速度PID控制对象
PID SevenPID = PID(PWM_MIN, PWM_MAX, Kp_seven, Ki_seven, Kd_seven);


int is_brake = 0;       // 为1则表示正在急停，为0则表示正常运动
int is_turning = 0;     // 为1则表示正在旋转，为0则表示正常运动
int move_state = 1;     // 运动状态，1为直行，2为后退，3为左移，4为右移

// 创建1个电池电压对象
Battery battery3S;


// 10ms定时中断函数，核心函数
void control() {
  sei();          // 全局中断开启

  // 获取电机速度
  #ifdef PINS_REVERSE
    newPulses[0] = -ENC[0].read();  // A
    newPulses[1] = ENC[1].read();   // B
    newPulses[2] = -ENC[2].read();  // C
    newPulses[3] = ENC[3].read();   // D
  #else
    newPulses[0] = ENC[0].read();   // A
    newPulses[1] = -ENC[1].read();  // B
    newPulses[2] = ENC[2].read();   // C
    newPulses[3] = -ENC[3].read();  // D
  #endif

  // 陀螺仪矫正pid控制器
  feedbackYawVel = get_yaw();
//  Serial.println(feedbackYawVel);
  outYawPWM = YawPID.Compute((int)targetYawPulses, (int)feedbackYawVel);
  if(outYawPWM > YawPWM_MAX){
      outYawPWM = YawPWM_MAX;
  }  
 
  // 将陀螺仪矫正速度加到编码器目标速度上，除5是为了将PWM转换为编码器脉冲数
  targetPulses[0] -= (outYawPWM - outYawPWM_old)/5;
  targetPulses[1] += (outYawPWM - outYawPWM_old)/5;
  targetPulses[2] -= (outYawPWM - outYawPWM_old)/5;
  targetPulses[3] += (outYawPWM - outYawPWM_old)/5;

  // 七路水平矫正pid控制器
  switch(move_state){
      case 1: feedbackSevenVel = get_seven(1); break;
      case 2: feedbackSevenVel = get_seven(2); break;
      case 3: feedbackSevenVel = get_seven(3); break;
      case 4: feedbackSevenVel = get_seven(4); break; 
  }
//  Serial.println(targetSevenPulses);
  outSevenPWM = SevenPID.Compute(targetSevenPulses, feedbackSevenVel);
  if(outSevenPWM > SevenPWM_MAX){
      outSevenPWM = SevenPWM_MAX;
  }
  if(is_turning == 1){
      outSevenPWM = 0;
      outSevenPWM_old = 0;
  }
  
  // 将陀螺仪矫正速度加到编码器目标速度上，除5（7）是为了将PWM转换为编码器脉冲数
  switch(move_state){
      case 1: {
          targetPulses[0] += (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[1] -= (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[2] -= (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[3] += (outSevenPWM - outSevenPWM_old)/5;
      } break;
      case 2: {
          targetPulses[0] -= (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[1] += (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[2] += (outSevenPWM - outSevenPWM_old)/5;
          targetPulses[3] -= (outSevenPWM - outSevenPWM_old)/5;
      } break;
      case 3: {
          targetPulses[0] += (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[1] += (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[2] += (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[3] += (outSevenPWM - outSevenPWM_old)/6.4;
      } break;
      case 4: {
          targetPulses[0] -= (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[1] -= (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[2] -= (outSevenPWM - outSevenPWM_old)/6.4;
          targetPulses[3] -= (outSevenPWM - outSevenPWM_old)/6.4;
      } break;
  }

  outYawPWM_old = outYawPWM;
  outSevenPWM_old = outSevenPWM;
  
  // 底盘电机编码器负反馈pid控制器
  for (int i = 0; i < WHEEL_NUM; i++) {
    feedbackVel[i] = (float)newPulses[i];
    outPWM[i] = VeloPID[i].Compute(targetPulses[i], feedbackVel[i]);
    ENC[i].write(0);    // 复位电机编码器速度为0
  }
  
  if(is_brake == 1) {        // 如果急停
    motors.motorsBrake();
  }
  else{                      // 如果正常运动
    if (battery3S.is_Volt_Low() == false) {
      motors.setSpeeds(outPWM[0], outPWM[1], outPWM[2], outPWM[3]);
    }
  }
  
//  // 打印控制，控制周期1000ms
//  static int print_Count;
//  if (++print_Count >= 100){
//    Serial.print(millis());       // 显示
//    Serial.print(",");
//    Serial.println(battery3S.read());      // 显示
//    for (int i = 0; i < WHEEL_NUM; i++) {
//      Serial.print(i);                     // 显示
//      Serial.print(":");
//      Serial.print(targetPulses[i]);    // 显示
//      Serial.print(",");
//      Serial.print(feedbackVel[i]);     // 显示
//      Serial.print(",");
//      Serial.println(outPWM[i]);        // 显示
//      print_Count = 0;
//    }
//  }
}

// 带闭环控制的运动函数
void move_pid(int speed1, int speed2, int speed3, int speed4)
{
//    Serial.println("@start controlling!");        // 显示
    if((speed1 != 0) && (speed2 != 0) && (speed3 != 0) && (speed4 != 0)){
      is_brake = 0;        // 取消急停模式
      
      targetPulses[0] = -speed1;
      targetPulses[1] = -speed2;
      targetPulses[2] = -speed3;
      targetPulses[3] = -speed4;
    }
    else{
      brake();
      targetPulses[0] = 0;targetPulses[1] = 0;targetPulses[2] = 0;targetPulses[3] = 0;
      outPWM[0] = 0;outPWM[1] = 0;outPWM[2] = 0;outPWM[3] = 0;
    }
}

// 直行
void forward(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志

    brake();
    resetPara();
    move_state = 1;
    is_turning = 0;
    
    // 先走一段，跨过黑线
    move_pid(forward_speed, forward_speed, forward_speed, forward_speed);
    delay_ms(500);
    
    while (1) {   
      if ((seven_left(4) == LOW) || (seven_right(4) == LOW)) {                      // 检测到白色背景，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && ((seven_left(4) == HIGH) && (seven_right(4) == HIGH))) {   // 由白色变为黑色线，计数一次
        temp_count ++;          
//        Serial.println(temp_count);                 
        flag = 0;
        if(temp_count < line_count){
          delay_ms(500);        // 先走一段，跨过黑线
        }
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
    }
}

// 后退
void back(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志

    brake();
    resetPara();
    move_state = 2;
    is_turning = 0;
    
    // 先走一段，跨过黑线
    move_pid(-back_speed, -back_speed, -back_speed, -back_speed);
    delay_ms(500);
    
    while (1) {   
      if ((seven_left(4) == LOW) || (seven_right(4) == LOW)) {                      // 检测到白色背景，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && ((seven_left(4) == HIGH) && (seven_right(4) == HIGH))) {   // 由白色变为黑色线，计数一次
        temp_count ++;          
//        Serial.println(temp_count);                 
        flag = 0;
        if(temp_count < line_count){
          delay_ms(500);        // 先走一段，跨过黑线
        }
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
    }
}

// 急停
void brake()
{
    is_brake = 1;        // 设置为急停模式
    motors.setSpeeds(0,0,0,0);
    targetPulses[0] = 0;targetPulses[1] = 0;targetPulses[2] = 0;targetPulses[3] = 0;
    outPWM[0] = 0;outPWM[1] = 0;outPWM[2] = 0;outPWM[3] = 0;
//    Serial.println("@@@brake");
    delay(5);
}

// 向左平移
void left(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志

    brake();
    resetPara();
    move_state = 3;
    is_turning = 0;
    
    // 先走一段，跨过黑线
    move_pid(-left_speed, left_speed, left_speed, -left_speed);
    delay_ms(500);
    
    while (1) {   
      if ((seven_front(4) == LOW) || (seven_back(4) == LOW)) {                      // 检测到白色背景，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && ((seven_front(4) == HIGH) && (seven_back(4) == HIGH))) {   // 由白色变为黑色线，计数一次
        temp_count ++;          
//        Serial.println(temp_count);                 
        flag = 0;
        if(temp_count < line_count){
          delay_ms(500);        // 先走一段，跨过黑线
        }
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
    }
}

// 向右平移
void right(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志

    brake();
    resetPara();
    move_state = 4;
    is_turning = 0;
    
    // 先走一段，跨过黑线
    move_pid(right_speed, -right_speed, -right_speed, right_speed);
    delay_ms(500);
    
    while (1) {   
      if ((seven_front(4) == LOW) || (seven_back(4) == LOW)) {                      // 检测到白色背景，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && ((seven_front(4) == HIGH) && (seven_back(4) == HIGH))) {   // 由白色变为黑色线，计数一次
        temp_count ++;          
//        Serial.println(temp_count);                 
        flag = 0;
        if(temp_count < line_count){
          delay_ms(500);        // 先走一段，跨过黑线
        }
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
    }
}

// 用于陀螺仪矫正的10ms定时中断函数（测试用）
void yaw_control() {
  sei();      // 全局中断开启
  // pid控制器
  feedbackYawVel = get_yaw();
  Serial.println(feedbackYawVel);
  outYawPWM = YawPID.Compute(targetYawPulses, feedbackYawVel);

  //电池电压正常的情况下启动电机并设置速度
  if(is_brake == 1) {        // 如果急停
    motors.motorsBrake();
  }
  else{                      // 如果正常运动
    if (battery3S.is_Volt_Low() == false) {
      if(outYawPWM > YawPWM_MAX){
          outYawPWM = YawPWM_MAX;
      }
      motors.setSpeeds(-outYawPWM, outYawPWM, -outYawPWM, outYawPWM);
    }
  }
}

// 左转
void left_turn(int left_angle)
{
    is_brake = 0;
    is_turning = 1;
    targetYawPulses -= left_angle;
    Serial.println("left_turn");
}

// 右转
void right_turn(int right_angle)
{
    is_brake = 0;
    is_turning = 1;
    targetYawPulses += right_angle;
    Serial.println("right_turn");
}

// 用于七路水平矫正的10ms定时中断函数（测试用）
void seven_control() 
{
  sei();      // 全局中断开启
  // pid控制器
  feedbackSevenVel = get_seven(1);
  Serial.println(feedbackSevenVel);
  outSevenPWM = SevenPID.Compute(targetSevenPulses, feedbackSevenVel);

  //电池电压正常的情况下启动电机并设置速度
  if(is_brake == 1) {        // 如果急停
    motors.motorsBrake();
  }
  else{                      // 如果正常运动
    if (battery3S.is_Volt_Low() == false) {
      if(outSevenPWM > SevenPWM_MAX){
          outSevenPWM = SevenPWM_MAX;
      }
      motors.setSpeeds(outSevenPWM, -outSevenPWM, -outSevenPWM, outSevenPWM);
    }
  }
}

// 获得七路读取值（加权和）
int get_seven(int witch)
{ 
  int sense_value = 0;
  int error = 0;
  switch(witch){
      case 1: sense_value = 1 * seven_front(1) + 3 * seven_front(2) + 5 * seven_front(3) + 7 * seven_front(4) + 
                      9 * seven_front(5) + 11 * seven_front(6) + 13 * seven_front(7); break;
      case 2: sense_value = 1 * seven_back(1) + 3 * seven_back(2) + 5 * seven_back(3) + 7 * seven_back(4) + 
                      9 * seven_back(5) + 11 * seven_back(6) + 13 * seven_back(7); break;
      case 3: sense_value = 1 * seven_left(1) + 3 * seven_left(2) + 5 * seven_left(3) + 7 * seven_left(4) + 
                      9 * seven_left(5) + 11 * seven_left(6) + 13 * seven_left(7); break;
      case 4: sense_value = 1 * seven_right(1) + 3 * seven_right(2) + 5 * seven_right(3) + 7 * seven_right(4) + 
                      9 * seven_right(5) + 11 * seven_right(6) + 13 * seven_right(7); break;
      default: sense_value = 0; break;
  }

  switch (sense_value) {
      case 1:  error = -3.6; break;
      case 4:  error = -3.6;   break;
      case 3:  error = -3.6; break;
      case 8:  error = -3.4;   break;
      case 5:  error = -2.8; break;
      case 12: error = -2;   break;
      case 7:  error = 0;    break;
      case 16: error = 2;    break;
      case 9:  error = 2.8;  break;
      case 20: error = 3.4;    break;
      case 11: error = 3.6;  break;
      case 24: error = 3.6;    break;
      case 13: error = 3.6;  break;
      default: error = 0;    break;
    }

  return error;
}

// 重置所有PID变量
void resetPara()
{
    VeloPID[0].UpdateParameters();
    VeloPID[1].UpdateParameters();
    VeloPID[2].UpdateParameters();
    VeloPID[3].UpdateParameters();
    YawPID.UpdateParameters();
    SevenPID.UpdateParameters();
    targetPulses[0] = 0;targetPulses[1] = 0;targetPulses[2] = 0;targetPulses[3] = 0;
    outPWM[0] = 0;outPWM[1] = 0;outPWM[2] = 0;outPWM[3] = 0;
    newYawPulses = 0;
    newSevenPulses = 0; targetSevenPulses = 0; 
}
