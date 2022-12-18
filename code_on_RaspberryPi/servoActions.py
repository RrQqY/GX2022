#coding:utf-8

import numpy as np
import time
import serial
from uservo import UartServoManager

class servoActions():
    """
    舵机动作类，动作方法如下：
    Get_pla1_pos1_up: 抓取货架①（场地下方）上层位置1         √
    Get_pla1_pos2_up：抓取货架①（场地下方）上层位置2         √
    Get_pla1_pos3_up：抓取货架①（场地下方）上层位置3         √
    Get_pla1_pos1_down：抓取货架①（场地下方）下层位置1       √
    Get_pla1_pos2_down：抓取货架①（场地下方）下层位置2       √
    Get_pla1_pos3_down：抓取货架①（场地下方）下层位置3       √
    Put_pla2_pos1：放置货架②（场地右侧）位置1                √
    Put_pla2_pos2：放置货架②（场地右侧）位置2                √
    Put_pla2_pos3：放置货架②（场地右侧）位置3                √
    Get_pla2_pos1：抓取货架②（场地右侧）位置1                √
    Get_pla2_pos2：抓取货架②（场地右侧）位置2                √
    Get_pla2_pos3：抓取货架②（场地右侧）位置3                √
    Put_pla3_pos1_down：放置货架③（场地上方）下层位置1       √
    Put_pla3_pos2_down：放置货架③（场地上方）下层位置2       √
    Put_pla3_pos3_down：放置货架③（场地上方）下层位置3       √
    Put_pla3_pos1_up：放置货架③（场地上方）上层位置1         √
    Put_pla3_pos2_up：放置货架③（场地上方）上层位置2         √
    Put_pla3_pos3_up：放置货架③（场地上方）上层位置3         √
    Depo_left_in：左货仓放入                               √
    Depo_left_out：左货仓取出                              √                 
    Depo_right_in：右货仓放入                              √
    Depo_right_out：右货仓取出                             √
    Depo_middle_in：中货仓放入                             √
    Depo_middle_out：中货仓取出                            √
    """

    def __init__(self):
        self.row = 4        # 4个动作
        self.col = 5        # 5个舵机

        SERVO_PORT_NAME =  u'/dev/ttyUSB0'		# 舵机串口号
        SERVO_BAUDRATE = 115200			        # 舵机的波特率
        self.SERVO_ID_0 = 0					    # 舵机的ID号
        self.SERVO_ID_1 = 1
        self.SERVO_ID_2 = 2
        self.SERVO_ID_3 = 3
        self.SERVO_ID_5 = 5
        self.SERVO_HAS_MTURN_FUNC = False	    # 舵机是否拥有多圈模式
        # 初始化串口
        self.servo_uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
                            parity=serial.PARITY_NONE, stopbits=1,\
                            bytesize=8,timeout=0)
        # 初始化舵机管理器
        self.uservo = UartServoManager(self.servo_uart, is_debug=True)

        self.decay = 0.95          # 整体速度缩放比例
        self.decay_time = 600      # 舵机减速时间

    # -------- 等待时间判断 --------
    # 进仓库等待时间判断
    def getDepoInDelayTime(self, time_sleep_flag='0to0'):
        """
        收入仓库旋转时间判断
        """
        if time_sleep_flag == '1to1':
            time_sleep = 1
        elif time_sleep_flag == '1to2':
            time_sleep = 1
        elif time_sleep_flag == '1to3':
            time_sleep = 1.6
        elif time_sleep_flag == '2to1':
            time_sleep = 1
        elif time_sleep_flag == '2to2':
            time_sleep = 1.2
        elif time_sleep_flag == '2to3':
            time_sleep = 1.8
        elif time_sleep_flag == '3to1':
            time_sleep = 1
        elif time_sleep_flag == '3to2':
            time_sleep = 1.4
        elif time_sleep_flag == '3to3':
            time_sleep = 2
        else:
            time_sleep = 2
        return (time_sleep + 0.2) / self.decay

    
    # 出仓库等待时间判断
    def getDepoOutDelayTime(self, time_sleep_flag='0to0'):
        """
        收入仓库旋转时间判断
        """
        if time_sleep_flag == '1to1':
            time_sleep = 1
        elif time_sleep_flag == '1to2':
            time_sleep = 0.8
        elif time_sleep_flag == '1to3':
            time_sleep = 1
        elif time_sleep_flag == '2to1':
            time_sleep = 1
        elif time_sleep_flag == '2to2':
            time_sleep = 1.2
        elif time_sleep_flag == '2to3':
            time_sleep = 1.4
        elif time_sleep_flag == '3to1':
            time_sleep = 1.6
        elif time_sleep_flag == '3to2':
            time_sleep = 1.8
        elif time_sleep_flag == '3to3':
            time_sleep = 2
        else:
            time_sleep = 2
        return (time_sleep + 0.2) / self.decay


    # -------- 与货架相关的动作 --------
    # 开始前机械臂动作
    start = [[0 for i in range(5)] for j in range(1)]             
    start = [[0, 0, 135, -40, 10]]
    def Servo_start(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.start[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.start[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.start[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.start[0][3],velocity=200.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.start[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.1)

    # 抓取准备（起始动作），1度
    prepare_1 = [[0 for i in range(5)] for j in range(1)]             
    prepare_1 = [[1, -10, 130, 30, -85]]
    def Servo_prepare_1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare_1[0][0],velocity=150.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare_1[0][1],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare_1[0][2],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare_1[0][3],velocity=200.0, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare_1[0][4],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1)

    # 抓取准备（起始动作），0度
    prepare_0 = [[0 for i in range(5)] for j in range(1)]             
    prepare_0 = [[0, -10, 130, 30, -85]]
    def Servo_prepare_0(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare_0[0][0],velocity=150.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare_0[0][1],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare_0[0][2],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare_0[0][3],velocity=200.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare_0[0][4],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.1)

    # 抓取准备（起始动作），0度
    prepare = [[0 for i in range(5)] for j in range(1)]             
    prepare = [[0, -10, 130, 30, -85]]
    def Servo_prepare(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare[0][0],velocity=150.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare[0][1],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare[0][2],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare[0][3],velocity=200.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare[0][4],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(3)

    # 结束时将机械臂抽到高处
    end_out = [[0 for i in range(5)] for j in range(1)]             
    end_out = [[90, 8, 70, -90, -80]]
    def Servo_end_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.end_out[0][0],velocity=150.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.end_out[0][1],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.end_out[0][2],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.end_out[0][3],velocity=200.0, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.end_out[0][4],velocity=100.0, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1)

    # 抓取货架①（场地下方）上层
    pla1_pos1_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置一
    pla1_pos2_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置二
    pla1_pos3_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置三
    pla1_pos1_up_get = [[66, 8, 120, 20, -80],       # 准备
                        [66, -50, 38, -3, -80],       # 伸到物块前
                        [66, -50, 38, -3, -115],      # 抓
                        [66, 8, 80, -70, -115]]      # 抓回到准备位置
    # 抓取货架①（场地下方）上层位置1
    def Get_pla1_pos1_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[0][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[1][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[1][2],velocity=300.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[1][3],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[2][4],velocity=200.0 * self.decay, t_acc=200, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[3][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[3][2],velocity=50.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[3][3],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla1_pos2_up_get = [[90, 8, 120, 20, -80],
                        [90, -37, 61, 5, -80],
                        [90, -37, 61, 5, -115],
                        [90, 8, 80, -70, -115]]
    # 抓取货架①（场地下方）上层位置2
    def Get_pla1_pos2_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[0][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[1][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[1][2],velocity=300.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[1][3],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[2][4],velocity=200.0 * self.decay, t_acc=200, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[3][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[3][2],velocity=50.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[3][3],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla1_pos3_up_get = [[114, 8, 120, 20, -80],
                        [114, -50, 38, -3, -80],
                        [114, -50, 38, -3, -115],
                        [114, 8, 80, -70, -115]]
    # 抓取货架①（场地下方）上层位置3
    def Get_pla1_pos3_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[0][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[0][3],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[1][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[1][2],velocity=300.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[1][3],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[2][4],velocity=200.0 * self.decay, t_acc=200, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[3][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[3][2],velocity=50.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[3][3],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    # 抓取货架①（场地下方）下层
    pla1_pos1_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置一
    pla1_pos2_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置二
    pla1_pos3_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置三
    pla1_pos1_down_get = [[66, -40, 122, 70, -80],      # 准备
                          [66, -69, 58, 41, -80],       # 伸到物块前
                          [66, -69, 58, 41, -115],       # 抓
                          [66, -24, 135, 38, -115]]      # 抓回到准备位置
    # pla1_pos1_down_get = [[66, -40, 122, 70, -80],      # 准备
    #                       [66, -73, 55, 41, -80],       # 伸到物块前
    #                       [66, -73, 55, 41, -115],       # 抓
    #                       [66, -24, 135, 38, -115]]      # 抓回到准备位置
    # 抓取货架①（场地下方）下层位置1
    def Get_pla1_pos1_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[0][0],velocity=175.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[0][1],velocity=100.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[0][2],velocity=50.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[0][3],velocity=140.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[1][0],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[1][1],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[1][2],velocity=250.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[1][3],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[1][4],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.8)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[2][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[3][0],velocity=100.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[3][1],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[3][2],velocity=150.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[3][3],velocity=70.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla1_pos2_down_get = [[90, -37, 135, 72, -80],
                          [90, -62, 84, 59, -80],
                          [90, -62, 84, 59, -115],
                          [90, -24, 125, 33, -115]]
    # 抓取货架①（场地下方）下层位置2
    def Get_pla1_pos2_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[0][0],velocity=175.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[0][1],velocity=100.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[0][2],velocity=50.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[0][3],velocity=140.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[1][0],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[1][1],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[1][2],velocity=250.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[1][3],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[1][4],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.8)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[2][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[3][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[3][3],velocity=70.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.6 / self.decay)


    pla1_pos3_down_get = [[114, -40, 122, 70, -80],
                          [114, -69, 58, 41, -80],
                          [114, -69, 58, 41, -115],
                          [114, -24, 135, 38, -115]]
    # 抓取货架①（场地下方）下层位置3
    def Get_pla1_pos3_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[0][0],velocity=175.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[0][1],velocity=100.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[0][2],velocity=50.0 * self.decay, t_acc=600, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[0][3],velocity=140.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[1][0],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[1][1],velocity=75.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[1][2],velocity=250.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[1][3],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[1][4],velocity=150.0 * self.decay * 0.8, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.8)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[2][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[3][0],velocity=100.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[3][1],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[3][2],velocity=150.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[3][3],velocity=70.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    # 放置货架②（场地右侧）
    pla2_pos1_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置一
    pla2_pos2_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置二
    pla2_pos3_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置三
    pla2_pos1_put = [[66, -5, 82, -30, -115],       # 先把物块移出去
                     [66, -45, 72, 35, -110],       # 放到色环正上方
                     [66, -79, 59, 39, -110],       # 放到色环上
                     [66, -79, 59, 39, -85],        # 松开
                     [66, -40, 121, 70, -85]]       # 缩回
    # 放置货架②（场地右侧）位置1
    def Put_pla2_pos1(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[0][1],velocity=80.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[0][3],velocity=100.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[1][2],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(2.3)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[2][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[2][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[4][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla2_pos2_put = [[93, -5, 82, -30, -115],        # 先把物块移出去
                     [93, -35, 99, 70, -110],
                     [93, -74, 84, 50, -110],
                     [93, -74, 84, 50, -85],
                     [93, -50, 120, 80, -85]]
    # 放置货架②（场地右侧）位置2
    def Put_pla2_pos2(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[0][1],velocity=80.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[0][3],velocity=100.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[1][2],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[2][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[2][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[4][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla2_pos3_put = [[115, -5, 82, -30, -115],       # 先把物块移出去
                     [115, -45, 72, 35, -110],       # 放到色环正上方
                     [115, -79, 59, 39, -110],       # 放到色环上
                     [115, -79, 59, 39, -85],        # 松开
                     [115, -40, 121, 70, -85]]       # 缩回
    # 放置货架②（场地右侧）位置3
    def Put_pla2_pos3(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[0][1],velocity=80.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[0][3],velocity=100.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[1][2],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[2][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[2][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[4][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    # 抓取货架②（场地右侧）
    pla2_pos1_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置一
    pla2_pos2_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置二
    pla2_pos3_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置三
    pla2_pos1_get = [[66, 0, 82, -30, -85],       # 先把物块移出去
                     [66, -58, 118, 82, -85],       # 准备
                     [66, -78, 48, 35, -85],        # 伸到物块前
                     [66, -78, 48, 35, -112],       # 抓
                     [66, 0, 80, -40, -112]]      # 拎起
    # 抓取货架②（场地右侧）位置1
    def Get_pla2_pos1(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[1][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[1][2],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[1][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1)
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[2][0],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[2][1],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[2][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[4][1],velocity=200.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[4][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)


    pla2_pos2_get = [[93, 0, 82, -30, -85],       # 先把物块移出去
                     [93, -61, 117, 85, -85],
                     [93, -68, 70, 41, -85],
                     [93, -68, 70, 41, -112],
                     [93, 0, 80, -40, -112]] 
    # 抓取货架②（场地右侧）位置2
    def Get_pla2_pos2(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[1][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[1][2],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[1][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[2][0],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[2][1],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[2][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[4][1],velocity=200.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[4][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)


    pla2_pos3_get = [[115, 0, 82, -30, -85],       # 先把物块移出去
                     [115, -58, 118, 82, -85],       # 准备
                     [115, -78, 48, 34, -85],        # 伸到物块前
                     [115, -78, 48, 34, -112],       # 抓
                     [115, 0, 80, -40, -112]]      # 拎起
    # 抓取货架②（场地右侧）位置3
    def Get_pla2_pos3(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[1][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[1][1],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[1][2],velocity=80.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[1][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(2.3)
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[2][0],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[2][1],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[2][3],velocity=200.0 * self.decay, t_acc=150, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[4][1],velocity=200.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[4][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)

    compen_angle = 1      # 场地上方台子

    # 放置货架③（场地上方）下层
    pla3_pos1_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置一
    pla3_pos2_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置二
    pla3_pos3_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置三
    pla3_pos1_down_put = [[58 + compen_angle, -5, 82, -30, -115],       # 先把物块移出去
                          [58 + compen_angle, -15, 135, 75, -110],       # 放到色环上方
                          [58 + compen_angle, -65, 120, 94, -110],       # 放到色环上
                          [58 + compen_angle, -65, 120, 94, -80],        # 松开
                          [58 + compen_angle, -20, 125, 70, -80]]        # 缩回
    # 放置货架③（场地上方）下层位置1
    def Put_pla3_pos1_down(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[1][3],velocity=250.0 * self.decay, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[2][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[2][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[2][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[2][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[3][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[4][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla3_pos2_down_put = [[90 + compen_angle, -5, 82, -30, -115],       # 先把物块移出去
                          [90 + compen_angle, -15, 135, 75, -110],
                          [90 + compen_angle, -42, 129, 65, -110],
                          [90 + compen_angle, -42, 129, 65, -80],
                          [90 + compen_angle, -12, 131, 60, -80]]
    # 放置货架③（场地上方）下层位置2
    def Put_pla3_pos2_down(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[1][3],velocity=250.0 * self.decay, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[2][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[2][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[2][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[2][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[3][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[4][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    pla3_pos3_down_put = [[121 + compen_angle, -5, 82, -30, -115],       # 先把物块移出去
                          [121 + compen_angle, -15, 135, 75, -110],
                          [121 + compen_angle, -66, 120, 94, -110],
                          [121 + compen_angle, -66, 120, 94, -80],
                          [121 + compen_angle, -20, 125, 70, -80]]
    # 放置货架③（场地上方）下层位置3
    def Put_pla3_pos3_down(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[1][3],velocity=250.0 * self.decay, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[2][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[2][1],velocity=195.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[2][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[2][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[2][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.4 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[3][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[4][0],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[4][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[4][2],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[4][3],velocity=50.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[4][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    # 放置货架③（场地上方）上层
    pla3_pos1_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置一
    pla3_pos2_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置二
    pla3_pos3_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置三
    pla3_pos1_up_put = [[58 + compen_angle, 0, 82, -10, -115],        # 先把物块移出去
                        [58 + compen_angle, -12, 95, 33, -110],       # 放到物块上方
                        [58 + compen_angle, -34, 122, 63, -110],       # 放到物块上
                        [58 + compen_angle, -34, 122, 63, -80],        # 松开
                        [58 + compen_angle, 8, 105, -40, -80]]          # 缩回
    # 放置货架③（场地上方）上层位置1
    def Put_pla3_pos1_up(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[1][2],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[2][0],velocity=200.0 * self.decay * 0.7, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[2][1],velocity=75.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[2][2],velocity=225.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[2][3],velocity=150.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[2][4],velocity=150.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[3][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[4][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[4][1],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[4][2],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[4][3],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[4][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)


    pla3_pos2_up_put = [[90 + compen_angle, 0, 82, -10, -115],        # 先把物块移出去
                        [90 + compen_angle, 0, 117, 43, -110],
                        [90 + compen_angle, -18, 134, 53, -110],
                        [90 + compen_angle, -18, 134, 53, -80],
                        [90 + compen_angle, 8, 90, -60, -80]]
    # 放置货架③（场地上方）上层位置2
    def Put_pla3_pos2_up(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[1][2],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[2][0],velocity=200.0 * self.decay * 0.7, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[2][1],velocity=195.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[2][2],velocity=200.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[2][3],velocity=150.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[2][4],velocity=150.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[3][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[4][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[4][1],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[4][2],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[4][3],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[4][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)


    pla3_pos3_up_put = [[121 + compen_angle, 0, 82, -10, -115],        # 先把物块移出去
                        [121 + compen_angle, -12, 95, 33, -110],
                        [121 + compen_angle, -34, 122, 63, -110],
                        [121 + compen_angle, -34, 122, 63, -80],
                        [121 + compen_angle, 8, 105, -40, -80]]
    # 放置货架③（场地上方）上层位置3
    def Put_pla3_pos3_up(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[0][1],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[0][2],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[0][3],velocity=200.0 * self.decay, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[0][4],velocity=200.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[1][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[1][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[1][2],velocity=75.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[1][3],velocity=250.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[1][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        # time.sleep(1.7)
        time_sleep = self.getDepoOutDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[2][0],velocity=200.0 * self.decay * 0.7, t_acc=50, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[2][1],velocity=75.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[2][2],velocity=225.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[2][3],velocity=75.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[2][4],velocity=150.0 * self.decay * 0.7, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(1 / self.decay / 0.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[3][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[3][2],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[3][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[3][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[4][0],velocity=200.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[4][1],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[4][2],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[4][3],velocity=225.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[4][4],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time.sleep(0.8 / self.decay)


    # -------- 与仓库相关的动作 --------
    # 放入
    depo_left_in =   [[0 for i in range(5)] for j in range(4)]      # 放入左货仓
    depo_middle_in = [[0 for i in range(5)] for j in range(4)]      # 放入中货仓
    depo_right_in =  [[0 for i in range(5)] for j in range(4)]      # 放入右货仓
    depo_left_in =   [[-90, -20, 57, -114, -112],       # 移到左仓库上方
                      [-90, -24, 103, -67, -112],       # 移到左仓库内
                      [-90, -24, 103, -67, -85],       # 松开
                      [-90, -20, 67, -104, -85]]       # 抬起到左仓库上方
    # depo_left_in =   [[-90, -20, 67, -104, -112],       # 移到左仓库上方
    #                   [-90, -24, 103, -67, -112],       # 移到左仓库内
    #                   [-90, -24, 103, -67, -85],       # 松开
    #                   [-90, -20, 67, -104, -85]]       # 抬起到左仓库上方

    # 左货仓放入
    def Depo_left_in(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[0][1],velocity=100.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[0][2],velocity=100.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[0][3],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[1][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    depo_middle_in = [[0, -20, 57, -114, -112],
                      [0, -24, 103, -67, -112],
                      [0, -24, 103, -67, -85],
                      [0, -20, 67, -104, -85]]
    # 中货仓放入
    def Depo_middle_in(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[0][1],velocity=100.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[0][2],velocity=100.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[0][3],velocity=165.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[1][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    depo_right_in = [[90, -20, 57, -114, -112],
                     [90, -24, 103, -67, -112],
                     [90, -24, 103, -67, -85],
                     [90, -20, 67, -104, -85]]
    # 右货仓放入
    def Depo_right_in(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[0][1],velocity=100.0 * self.decay, t_acc=200, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[0][2],velocity=100.0 * self.decay, t_acc=10, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[0][3],velocity=160.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        #time.sleep(2.7)
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[1][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[2][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)


    # 取出
    depo_left_out =   [[0 for i in range(5)] for j in range(4)]      # 拿出左货仓
    depo_middle_out = [[0 for i in range(5)] for j in range(4)]      # 拿出中货仓
    depo_right_out =  [[0 for i in range(5)] for j in range(4)]      # 拿出右货仓
    depo_left_out =   [[-90, -20, 67, -96, -85],       # 移到左仓库上方
                       [-90, -24, 96, -72, -85],       # 移到左仓库内
                       [-90, -24, 96, -72, -115],       # 抓
                       [-90, -20, 67, -96, -115]]       # 抬起到左仓库上方
    # depo_left_out =   [[-90, -20, 67, -96, -85],       # 移到左仓库上方
    #                    [-90, -24, 103, -62, -85],       # 移到左仓库内
    #                    [-90, -24, 103, -62, -115],       # 抓
    #                    [-90, -20, 67, -96, -115]]       # 抬起到左仓库上方
    # 左货仓取出
    def Depo_left_out(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[0][3],velocity=180.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[1][3],velocity=180.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[2][4],velocity=150.0 * self.decay, t_acc=150, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[3][1],velocity=150.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[3][3],velocity=180.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.7 / self.decay)


    depo_middle_out = [[0, -20, 67, -100, -85],
                       [0, -24, 96, -72, -85],
                       [0, -24, 96, -72, -115],
                       [0, -10, 60, -100, -115]]
    # 中货仓取出
    def Depo_middle_out(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[0][3],velocity=180.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[1][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[2][4],velocity=150.0 * self.decay, t_acc=150, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.7 / self.decay)


    depo_right_out = [[90, -20, 67, -100, -85],
                      [90, -24, 96, -72, -85],
                      [90, -24, 96, -72, -115],
                      [90, -20, 67, -100, -115]]
    # 右货仓取出
    def Depo_right_out(self, time_sleep_flag):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[0][0],velocity=150.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[0][1],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[0][2],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[0][3],velocity=180.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[0][4],velocity=100.0 * self.decay, t_acc=100, t_dec=self.decay_time)
        # self.uservo.wait()
        time_sleep = self.getDepoInDelayTime(time_sleep_flag)
        time.sleep(time_sleep)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[1][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[1][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[1][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[1][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[1][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[2][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[2][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[2][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[2][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[2][4],velocity=150.0 * self.decay, t_acc=150, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.6 / self.decay)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[3][0],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[3][1],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[3][2],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[3][3],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[3][4],velocity=100.0 * self.decay, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.7 / self.decay)
