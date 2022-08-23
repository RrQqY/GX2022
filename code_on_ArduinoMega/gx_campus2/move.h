#ifndef __MOVE_H
#define __MOVE_H


// 电机负反馈PID参数
#define  Kp  6
#define  Ki  0.3
#define  Kd  0
// 陀螺仪矫正PID参数
#define  Kp_yaw  4.6
#define  Ki_yaw  0.01
#define  Kd_yaw  0
// 七路矫正PID参数
#define  Kp_seven  16
#define  Ki_seven  0.05
#define  Kd_seven  0
// 巡线PID参数
#define  Kp_move  30
#define  Ki_move  2
#define  Kd_move  0

#define  YawPWM_MAX    60
#define  SevenPWM_MAX  80


// 运动速度宏定义
#define  forward_speed      10
#define  back_speed         10
#define  left_speed         14
#define  right_speed        14
#define  pre_slow_speed     2
#define  left_turn_speed    9
#define  right_turn_speed   9
#define  pre_slow_turn_speed   3


extern float targetPulses[4];
extern float targetYawPulses;
extern int   is_brake;
extern int   is_turning;
extern int   move_state;

extern void control();
extern void move_pid(int speed1, int speed2, int speed3, int speed4);      // 带闭环控制的运动函数
extern void forward(int line_count);             // 直行
extern void back(int line_count);                // 后退
extern void left(int line_count);                // 左平移
extern void right(int line_count);               // 右平移
extern void brake();                             // 急停
extern void left_turn(int left_angle);           // 左转
extern void right_turn(int right_angle);         // 右转
extern void resetPara();                         // 重置所有PID变量

#endif
