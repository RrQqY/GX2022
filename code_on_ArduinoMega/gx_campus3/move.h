#ifndef __MOVE_H
#define __MOVE_H

// 电机负反馈PID参数
#define  Kp             10      // 8
#define  Ki             0.3    // 0.3
#define  Kd             0
// 陀螺仪矫正PID参数
#define  Kp_yaw         6    // 5.2
#define  Ki_yaw         0
#define  Kd_yaw         0
// 七路矫正PID参数
#define  Kp_seven       9.6
#define  Ki_seven       0
#define  Kd_seven       0
// 转弯PID参数
#define  Kp_yaw_turn    2
#define  Ki_yaw_turn    0
#define  Kd_yaw_turn    0

#define  YawPWM_MAX            60
#define  SevenPWM_MAX          80
#define  YawPWM_turn_MAX       8

// 运动速度宏定义
#define  forward_speed         14
#define  back_speed            14
#define  left_speed            16
#define  right_speed           16

#define  forward_speed_slow    13
#define  back_speed_slow       13
#define  left_speed_slow       12
#define  right_speed_slow      12

#define  pre_slow_speed        2
#define  left_turn_speed       13
#define  right_turn_speed      13
#define  pre_slow_turn_speed   8

#define  forward_speed_align   7
#define  back_speed_align      7
#define  left_speed_align      7
#define  right_speed_align     7

// 转向时提前停下的角度
#define  pre_stop_turn         15


extern float targetPulses[4];
extern float targetYawPulses;        // 用于控制车身的目标朝向角
extern int   is_brake;
extern int   is_turning;
extern int   move_state;
extern int   left_turn_num;

extern void control();
extern void move_pid(int speed1, int speed2, int speed3, int speed4);      // 带闭环控制的运动函数
extern void forward(int line_count);             // 直行
extern void back(int line_count);                // 后退
extern void left(int line_count);                // 左平移
extern void right(int line_count);               // 右平移
extern void brake();                             // 急停
extern void left_turn(float left_angle);         // 左转
extern void right_turn(float right_angle);       // 右转
extern void align();                             // 对正函数
extern void resetPara();                         // 重置所有PID变量
extern void PID_forward(int clear_flag);         // 前进方向的PID
extern void PID_back(int clear_flag);            // 后退方向的PID
extern void PID_left(int clear_flag);            // 左移方向的PID
extern void PID_right(int clear_flag);           // 右移方向的PID
extern void PID_left_turn();                     // 左转的PID
extern void PID_right_turn();                    // 右转的PID
extern void right_to_rs();                       // 右移至右七路压线
extern void right_to_ls();                       // 右移至左七路压线
extern void left_to_rs();                        // 左移至右七路压线
extern void left_to_ls();                        // 左移至左七路压线
extern void forward_align_ls();                  // 直行方向上矫准（用左七路）
extern void forward_align_rs();                  // 直行方向上矫准（用右七路）

#endif
