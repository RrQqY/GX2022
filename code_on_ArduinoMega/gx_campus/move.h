#ifndef __MOVE_H
#define __MOVE_H

// 运动速度宏定义
#define  forward_speed      30
#define  back_speed         30
#define  left_slide_speed   30
#define  right_slide_speed  30
#define  pre_slow_speed     5
#define  left_turn_speed    14
#define  right_turn_speed   14
#define  pre_slow_turn_speed   3

// PID参数
#define  KP  10
#define  KI  1
#define  KD  0

extern float targetPulses[4];
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
