#ifndef __IMU_H
#define __IMU_H

#include "SunConfig.h"       // 包含配置库

extern void imu_setup();     // IMU初始化
extern float get_yaw();      // IMU获取yaw角数据

#endif
