/* 这里存储一些和底盘运动控制有关的函数 */
#include "gx_campus.h"


// 创建4个编码器对象
// 良好性能，只有第一个引脚具备外部中断能力
Encoder ENC[4] = {
    Encoder(ENCODER_A, DIRECTION_A), Encoder(ENCODER_B, DIRECTION_B),
    Encoder(ENCODER_C, DIRECTION_C), Encoder(ENCODER_D, DIRECTION_D)};
long newPulses[4] = {0, 0, 0, 0};  //四个车轮的定时中断编码器四倍频速度

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
float targetPulses[4] = {0, 0, 0, 0};
float feedbackVel[4] = {0, 0, 0, 0};
float Kp = 6, Ki = 0.3, Kd = 0;
double outPWM[4] = {0, 0, 0, 0};
PID VeloPID[4] = {
    PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd), PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd),
    PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd), PID(PWM_MIN, PWM_MAX, Kp, Ki, Kd)};

int is_brake = 0;     // 为1则表示急停，为0则表示正常运动

// 创建1个电池电压对象
Battery battery3S;


// 10ms定时中断函数，核心函数
void control() {
  sei();      // 全局中断开启

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
  
  // pid控制器
  for (int i = 0; i < WHEEL_NUM; i++) {
    feedbackVel[i] = (float)newPulses[i];
    outPWM[i] = VeloPID[i].Compute(targetPulses[i], feedbackVel[i]);
    ENC[i].write(0);    // 复位电机编码器速度为0
  }

  //电池电压正常的情况下启动电机并设置速度
  
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
      targetPulses[0] = -speed1;
      targetPulses[1] = -speed2;
      targetPulses[2] = -speed3;
      targetPulses[3] = -speed4;
      is_brake = 0;        // 取消急停模式
      delay(5);
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
    
    // 先走一段，跨过黑线
    move_pid(forward_speed, forward_speed, forward_speed, forward_speed);
    delay(500);
    
    while (1) {   
      if (seven_left(4) == LOW) {                               // 检测到黑色，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && (seven_left(4) == HIGH)) {             // 由黑色变为白色，计数一次
        temp_count ++;                          
        if(temp_count < line_count){
          // 先走一段，跨过黑线
          move_pid(forward_speed, forward_speed, forward_speed, forward_speed);
          delay(100);
        }
        flag = 0;
      }
      
      // 在线前提前减速
      if ((seven_left(7) == HIGH) || (seven_right(7) == HIGH)) {         // 中间前灰度数到线时先减速
        move_pid(forward_speed-pre_slow_speed, forward_speed-pre_slow_speed, forward_speed-pre_slow_speed, forward_speed-pre_slow_speed);
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
      
      PID_forward();           // 直行时矫正偏移
   }
}

// 后退
void back(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志
    
    // 先走一段，跨过黑线
    move_pid(-back_speed, -back_speed, -back_speed, -back_speed);
    delay(500);
    
    while (1) {   
      if (seven_left(4) == LOW) {                               // 检测到黑色，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && (seven_left(4) == HIGH)) {             // 由黑色变为白色，计数一次
        temp_count ++;                          
        if(temp_count < line_count){
          // 先走一段，跨过黑线
          move_pid(-back_speed, -back_speed, -back_speed, -back_speed);
          delay(100);
        }
        flag = 0;
      }
      
      // 在线前提前减速
      if ((seven_left(1) == HIGH) || (seven_right(7) == HIGH)) {         // 中间前灰度数到线时先减速
        move_pid(-back_speed+pre_slow_speed, -back_speed+pre_slow_speed, -back_speed+pre_slow_speed, -back_speed+pre_slow_speed);
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
      
      PID_back();           // 后退时矫正偏移
   }
}

// 急停
void brake()
{
    is_brake = 1;        // 设置为急停模式
//    Serial.println("@@@brake");
    delay(5);
}

// 向左平移
void left_slide(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志
    
    // 先走一段，跨过黑线
    move_pid(-left_slide_speed, left_slide_speed, left_slide_speed, -left_slide_speed);
    delay(500);
    
    while (1) {   
      if (seven_front(4) == LOW) {                               // 检测到黑色，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && (seven_front(4) == HIGH)) {             // 由黑色变为白色，计数一次
        temp_count ++;                          
        if(temp_count < line_count){
          // 先走一段，跨过黑线
          move_pid(-left_slide_speed, left_slide_speed, left_slide_speed, -left_slide_speed);
          delay(100);
        }
        flag = 0;
      }
      
      // 在线前提前减速
      if ((seven_front(1) == HIGH) || (seven_back(7) == HIGH)) {         // 中间前灰度数到线时先减速
        move_pid(-left_slide_speed+pre_slow_speed, left_slide_speed-pre_slow_speed, left_slide_speed-pre_slow_speed, -left_slide_speed+pre_slow_speed);
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
      
      PID_left();           // 左移时矫正偏移
   }
}

// 向右平移
void right_slide(int line_count)
{
    int temp_count = 0;                     // 当前所在线数
    int flag = 0;                           // 开始计数标志
    
    // 先走一段，跨过黑线
    move_pid(right_slide_speed, -right_slide_speed, -right_slide_speed, right_slide_speed);
    delay(500);
    
    while (1) {   
      if (seven_front(4) == LOW) {                               // 检测到黑色，开启计数准备
        flag = 1;
      }
      if ((flag == 1) && (seven_front(4) == HIGH)) {             // 由黑色变为白色，计数一次
        temp_count ++;                          
        if(temp_count < line_count){
          // 先走一段，跨过黑线
          move_pid(right_slide_speed, -right_slide_speed, -right_slide_speed, right_slide_speed);
          delay(100);
        }
        flag = 0;
      }
      
      // 在线前提前减速
      if ((seven_front(7) == HIGH) || (seven_back(1) == HIGH)) {         // 中间前灰度数到线时先减速
        move_pid(right_slide_speed-pre_slow_speed, -right_slide_speed+pre_slow_speed, -right_slide_speed+pre_slow_speed, right_slide_speed-pre_slow_speed);
      }
      
      // 数到对应的根数退出循环
      if (temp_count >= line_count) {
        brake();
        return;
      }
      
      PID_right();           // 右移时矫正偏移
   }
}

// 用于直行时矫正偏移的PID
void PID_forward()
{
    static int sensor[7];
    static double error = 0;
    static double P = 0, I = 0, D = 0;
    static double Kp = KP, Ki = KI, Kd = KD;         // PID 系数
    static double PID_value;
    static int previous_error = 0;
    
    sensor[0] = seven_front(1);
    sensor[1] = seven_front(2);
    sensor[2] = seven_front(3);
    sensor[3] = seven_front(4);
    sensor[4] = seven_front(5);
    sensor[5] = seven_front(6);
    sensor[6] = seven_front(7);
  
    static int switch_value = 0;
    switch_value = 1 * sensor[0] + 3 * sensor[1] + 5 * sensor[2] + 7 * sensor[3] + 9 * sensor[4] + 11 * sensor[5] + 13 * sensor[6];
    switch (switch_value) {
      case 48:error = -3.5; break;
      case 45:error = -3; break;
      case 40:error = -2.5; break;
      case 41:error = -2; break;
      case 34:error = -1.5; break;
      case 37:error = -1; break;
      case 28:error = -0; break;
      case 33:error = 1; break;
      case 22:error = 1.5; break;
      case 29:error = 2; break;
      case 16:error = 2.5; break;
      case 25:error = 3; break;
      case 36:error = 3.5; break;
      case 49:if (error == 3) error = 3.5;
              else if (error == -3) error = -3.5;
              else error = 0;
              break;
      default:error = 0;break;
    }
    
    P = error;
    I = I + error;
    D = error - previous_error;
    PID_value = Kp * P + Ki * I + Kd * D;
    previous_error = error;

    if(PID_value > 0){          // 如果大于0，左侧压线，应该向左移动
      move_pid(-left_slide_speed, left_slide_speed, left_slide_speed, -left_slide_speed);
    }
    else if(PID_value < 0){     // 如果小于0，右侧压线，应该向右移动
      move_pid(right_slide_speed, -right_slide_speed, -right_slide_speed, right_slide_speed);
    }
    else{                       // 如果等于0，中间压线，继续直走
      move_pid(forward_speed, forward_speed, forward_speed, forward_speed);
    }
}

// 用于后退时矫正偏移的PID
void PID_back()
{
      
}

// 用于左移时矫正偏移的PID
void PID_left()
{
      
}

// 用于右移时矫正偏移的PID
void PID_right()
{
      
}

// 左转
void left_turn(int left_angle)
{
    int left_target_angle;
    int left_yaw = 0;
    left_target_angle = (int)get_yaw() - left_angle + 7;     // 计算目标角度

    while(1){	 
      left_yaw = (int)get_yaw();        // 获取当前yaw值
      if(left_yaw > left_target_angle){
        // 开始左转
        Serial.println(left_yaw);
        move_pid(-left_turn_speed, left_turn_speed, -left_turn_speed, left_turn_speed);
        if(left_yaw < left_target_angle + 20){
            move_pid(right_turn_speed-pre_slow_turn_speed, -(right_turn_speed-pre_slow_turn_speed), 
                     right_turn_speed-pre_slow_turn_speed, -(right_turn_speed-pre_slow_turn_speed));
        }
      }
      else{
        brake();
        return;
      }
    }
}

// 右转
void right_turn(int right_angle)
{
    int right_target_angle;
    int right_yaw = 0; 
    right_target_angle = (int)get_yaw() + right_angle - 7;     // 计算目标角度

    while(1){	
      right_yaw = (int)get_yaw();        // 获取当前yaw值
      if(right_yaw < right_target_angle){
        // 开始右转
        Serial.println(right_yaw);
        move_pid(right_turn_speed, -right_turn_speed, right_turn_speed, -right_turn_speed);
        if(right_yaw > right_target_angle - 20){
            move_pid(right_turn_speed-pre_slow_turn_speed, -(right_turn_speed-pre_slow_turn_speed), 
                     right_turn_speed-pre_slow_turn_speed, -(right_turn_speed-pre_slow_turn_speed));
        }
      }
      else{
        brake();
        return;
      }
    }
}
