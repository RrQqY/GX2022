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
#define  Kp_seven  18
#define  Ki_seven  0.05
#define  Kd_seven  0
// 巡线PID参数
#define  Kp_move  30
#define  Ki_move  2
#define  Kd_move  0


// 运动速度宏定义
#define  forward_speed      12
#define  back_speed         12
#define  left_slide_speed   12
#define  right_slide_speed  12
#define  pre_slow_speed     2
#define  left_turn_speed    12
#define  right_turn_speed   12
#define  pre_slow_turn_speed   3


extern float targetPulses[4];
extern float targetYawPulses;
extern int   is_brake;

extern void control();
extern void move_pid(int speed1, int speed2, int speed3, int speed4);      // 带闭环控制的运动函数
extern void forward(int line_count);             // 直行
extern void back(int line_count);                // 后退
extern void brake();                             // 急停
extern void left_slide(int line_count);          // 向左平移
extern void right_slide(int line_count);         // 向右平移
extern void left_turn(int left_angle);           // 左转
extern void right_turn(int right_angle);         // 右转
extern void PID_forward();                       // 用于直行时矫正偏移的PID
extern void PID_back();                          // 用于后退时矫正偏移的PID
extern void PID_left();                          // 用于左移时矫正偏移的PID
extern void PID_right();                         // 用于右移时矫正偏移的PID


#endif
