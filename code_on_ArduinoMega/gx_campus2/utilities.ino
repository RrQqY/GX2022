/* 这里存储一些和其余功能的函数 */
#include "gx_campus2.h"


void delay_ms(long ms){
    unsigned long time_now = 0;

    time_now = millis();
    while(millis() < time_now + ms){
        ;
    }

}
