#ifndef __GX_CAMPUS_H
#define __GX_CAMPUS_H

#include "SunConfig.h"
#include <FlexiTimer2.h>  //定时中断
#include "move.h"
#include "gpio.h"
#include "imu.h"
#include "utilities.h"
#include "pi.h"

extern A4950MotorShield motors;

extern void prepare();      // 准备函数
extern void start();        // 开始函数

#endif
