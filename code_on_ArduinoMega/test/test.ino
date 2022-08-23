/* 测试代码 */
#include "test.h"

A4950MotorShield motors;


void setup()
{
  // 串口初始化
  Serial.begin(115200);
  Serial2.begin(115200);        // 与树莓派上位机通信串口初始化
}


// 准备函数
void prepare()
{
    
}


// 开始函数
void start()
{
  Serial2.write("1");
  Serial.println("print completed");
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
