/* 2022.09工程训练大赛校赛代码 */
#include "gx_campus.h"

A4950MotorShield motors;


void setup()
{
  // 底盘电机初始化
  motors.init();       //电机初始化，初始化引脚模式和pwm频率和电机死区
  delay(100);                               // 延时等待初始化完成
  FlexiTimer2::set(TIMER_PERIOD, control);  // 10毫秒定时中断函数
  FlexiTimer2::start();                     // 中断使能
  delay(100);                               // 延时等待初始化完成

  // 底盘IO初始化
  pinMode(start_key, INPUT);    // 开始按钮初始化
  seven_init();                 // 七路初始化
  
  // 串口初始化
  Serial.begin(BAUDRATE);
  Serial2.begin(115200);        // 与树莓派上位机通信串口初始化

  // IMU初始化
  imu_setup();
}


// 准备函数
void prepare()
{
    
}


// 开始函数
void start()
{
  // move_pid(40,40,40,40);
  // delay(3000);
  // move_pid(-40,-40,-40,-40);
  // delay(3000);
  // move_pid(40,-40,-40,40);
  // delay(3000);
  // move_pid(0,0,0,0);
  // delay(3000);

  // float yaw = 0.0;
  // while(1){
  //   yaw = get_yaw();
  //   Serial.println(yaw);
  // }

  right_turn(90);
  delay(5000);
  
  Serial.println("@@@");
  
  move_pid(20,20,20,20);
  delay(500);
  
  left_turn(90);
  
  Serial.println("@@@@@");
}


void loop()
{
//  prepare();                                        // 运行准备阶段函数
  while(1){
    if(digitalRead(start_key) == HIGH){
      start();                                      // 运行开始阶段函数
      break;
    }
    else if(digitalRead(start_key) == LOW){
      ;
    }
  }

  while(1){ 
  };
}
