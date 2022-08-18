/* 这里存储一些和其余功能的函数 */
#include "gx_campus2.h"


void delay_ms(int ms){
    int i = 0;
    while(i < ms * 2){
      i++;
      Serial.println(i);
    }
}
