#coding:utf-8

import numpy as np
import time
import serial
from uservo import UartServoManager

class servoActions():

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

    # -------- 与货架相关的动作 --------
    # 抓取准备（起始动作）
    prepare = [[0 for i in range(5)] for j in range(1)]             
    prepare = [[0, 0, 90, 90, -100]]

    # 抓取货架①（场地下方）上层
    pla1_pos1_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置一
    pla1_pos2_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置二
    pla1_pos3_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置三
    pla1_pos1_up_get = [[68, 8, 120, 10, -100],       # 准备
                        [68, -40, 53, 0, -100],       # 伸到物块前
                        [68, -40, 53, 0, -115],       # 抓
                        [68, 8, 120, 10, -115]]       # 抓回到准备位置
    # 抓取货架①（场地下方）上层位置1
    def get_pla1_pos1_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla1_pos2_up_get = [[90, 8, 120, 10, -100],
                        [90, -38, 66, 6, -100],
                        [90, -38, 66, 6, -115],
                        [90, 8, 120, 10, -115]]
    
    # 抓取货架①（场地下方）上层位置2
    def get_pla1_pos2_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla1_pos3_up_get = [[114, 8, 120, 10, -100],
                        [114, -40, 50, 0, -100],
                        [114, -40, 50, 0, -115],
                        [114, 8, 120, 10, -115]]
    # 抓取货架①（场地下方）上层位置3
    def get_pla1_pos3_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 抓取货架①（场地下方）下层
    pla1_pos1_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置一
    pla1_pos2_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置二
    pla1_pos3_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置三
    pla1_pos1_down_get = [[68, -40, 122, 57, -100],      # 准备
                          [68, -65, 68, 36, -100],       # 伸到物块前
                          [68, -65, 68, 36, -115],       # 抓
                          [68, -40, 135, 78, -115]]      # 抓回到准备位置
    # 抓取货架①（场地下方）下层位置1
    def get_pla1_pos1_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla1_pos2_down_get = [[90, -37, 135, 68, -100],
                          [90, -56, 89, -48, -100],
                          [90, -56, 89, -48, -115],
                          [90, -32, 135, 66, -115]]
    # 抓取货架①（场地下方）下层位置2
    def get_pla1_pos2_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla1_pos3_down_get = [[114, -40, 122, 57, -100],
                          [114, -65, 68, 36, -100],
                          [114, -65, 68, 36, -115],
                          [114, -40, 135, 78, -115]]
    # 抓取货架①（场地下方）下层位置3
    def get_pla1_pos3_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 放置货架②（场地右侧）
    pla2_pos1_put = [[0 for i in range(5)] for j in range(4)]         # 放置货架②位置一
    pla2_pos2_put = [[0 for i in range(5)] for j in range(4)]         # 放置货架②位置二
    pla2_pos3_put = [[0 for i in range(5)] for j in range(4)]         # 放置货架②位置三
    pla2_pos1_put = [[68, -73, 57, 25, -115],       # 放到色环正上方
                    [68, -83, 56, 37, -115],       # 放到色环上
                    [68, -83, 56, 37, -100],       # 松开
                    [68, -55, 121, 70, -100]]      # 缩回
    # 放置货架②（场地右侧）位置1
    def put_pla2_pos1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla2_pos2_put = [[90, -64, 84, 45, -115],
                    [90, -73, 81, 48, -115],
                    [90, -73, 81, 48, -100],
                    [90, -61, 117, 73, -100]]
    # 放置货架②（场地右侧）位置2
    def put_pla2_pos2(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla2_pos3_put = [[114, -73, 57, 25, -115],
                    [114, -83, 56, 37, -115],
                    [114, -83, 56, 37, -100],
                    [114, -55, 121, 70, -100]]
    # 放置货架②（场地右侧）位置3
    def put_pla2_pos3(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 抓取货架②（场地右侧）
    pla2_pos1_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置一
    pla2_pos2_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置二
    pla2_pos3_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置三
    pla2_pos1_get = [[68, -55, 121, 70, -100],       # 准备
                    [68, -75, 56, 37, -100],        # 伸到物块前
                    [68, -75, 56, 37, -115],        # 抓
                    [68, -20, 72, -100, -115]]      # 拎起
    # 抓取货架②（场地右侧）位置1
    def get_pla2_pos1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla2_pos2_get = [[90, -61, 117, 73, -100],
                    [90, -66, 81, 48, -100],
                    [90, -66, 81, 48, -115],
                    [90, -20, 72, -100, -115]] 
    # 抓取货架②（场地右侧）位置2
    def get_pla2_pos2(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla2_pos3_get = [[114, -55, 121, 70, -100],
                    [114, -75, 56, 37, -100],
                    [114, -75, 56, 37, -115],
                    [114, -20, 72, -100, -115]]
    # 抓取货架②（场地右侧）位置3
    def get_pla2_pos3(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 放置货架③（场地上方）下层
    pla3_pos1_down_put = [[0 for i in range(5)] for j in range(4)]    # 放置货架③下层位置一
    pla3_pos2_down_put = [[0 for i in range(5)] for j in range(4)]    # 放置货架③下层位置二
    pla3_pos3_down_put = [[0 for i in range(5)] for j in range(4)]    # 放置货架③下层位置三
    pla3_pos1_down_put = [[58, -50, 124, 77, -115],       # 放到色环上方
                          [58, -66, 122, 90, -115],       # 放到色环上
                          [58, -66, 122, 90, -80],        # 松开
                          [58, -39, 120, 55, -80]]        # 缩回
    # 放置货架③（场地上方）下层位置1
    def put_pla3_pos1_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla3_pos2_down_put = [[90, -44, 135, 81, -115],
                          [90, -59, 135, 92, -115],
                          [90, -59, 135, 92, -80],
                          [90, -17, 131, 43, -80]]
    # 放置货架③（场地上方）下层位置2
    def put_pla3_pos2_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla3_pos3_down_put = [[122, -50, 124, 77, -115],
                        [122, -66, 122, 90, -115],
                        [122, -66, 122, 90, -80],
                        [122, -39, 120, 55, -80]]
    # 放置货架③（场地上方）下层位置3
    def put_pla3_pos3_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 放置货架③（场地上方）上层
    pla3_pos1_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置一
    pla3_pos2_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置二
    pla3_pos3_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置三
    pla3_pos1_up_put = [[58, -17, 115, 36, -115],       # 放到物块上方
                        [58, -33, 128, 64, -115],       # 放到物块上
                        [58, -33, 128, 64, -80],        # 松开
                        [58, 8, 135, 33, -80]]          # 缩回
    # 放置货架③（场地上方）上层位置1
    def put_pla3_pos1_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla3_pos2_up_put = [[90, -9, 135, 45, -115],
                        [90, -20, 135, 49, -115],
                        [90, -20, 135, 49, -80],
                        [90, 8, 126, 20, -80]]
    # 放置货架③（场地上方）上层位置2
    def put_pla3_pos2_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    pla3_pos3_up_put = [[122, -17, 115, 36, -115],
                        [122, -33, 128, 64, -115],
                        [122, -33, 128, 64, -80],
                        [122, 8, 135, 33, -80]]
    # 放置货架③（场地上方）上层位置3
    def put_pla3_pos3_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # -------- 与仓库相关的动作 --------
    # 放入
    depo_left_in =   [[0 for i in range(5)] for j in range(4)]      # 放入左货仓
    depo_middle_in = [[0 for i in range(5)] for j in range(4)]      # 放入中货仓
    depo_right_in =  [[0 for i in range(5)] for j in range(4)]      # 放入右货仓
    depo_left_in =   [[-90, -20, 72, -100, -115],       # 移到左仓库上方
                      [-90, -24, 103, -67, -115],       # 移到左仓库内
                      [-90, -24, 103, -67, -100],       # 松开
                      [-90, -20, 72, -100, -100]]       # 抬起到左仓库上方
    def depo_left_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    depo_middle_in = [[0, -20, 72, -100, -115],
                      [0, -24, 103, -67, -115],
                      [0, -24, 103, -67, -100],
                      [0, -20, 72, -100, -100]]
    # 中货仓放入
    def depo_middle_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    depo_right_in = [[90, -20, 72, -100, -115],
                     [90, -24, 103, -67, -115],
                     [90, -24, 103, -67, -100],
                     [90, -20, 72, -100, -100]]
    # 右货仓放入
    def depo_right_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    # 取出
    depo_left_out =   [[0 for i in range(5)] for j in range(4)]      # 拿出左货仓
    depo_middle_out = [[0 for i in range(5)] for j in range(4)]      # 拿出中货仓
    depo_right_out =  [[0 for i in range(5)] for j in range(4)]      # 拿出右货仓
    depo_left_out =   [[-90, -20, 72, -100, -100],       # 移到左仓库上方
                       [-90, -24, 103, -67, -100],       # 移到左仓库内
                       [-90, -24, 103, -67, -115],       # 抓
                       [-90, -20, 72, -100, -115]]       # 抬起到左仓库上方
    # 左货仓取出
    def depo_left_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    depo_middle_out = [[0, -20, 72, -100, -100],
                       [0, -24, 103, -67, -100],
                       [0, -24, 103, -67, -115],
                       [0, -20, 72, -100, -115]]
    # 中货仓取出
    def depo_middle_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()


    depo_right_out = [[90, -20, 72, -100, -100],
                      [90, -24, 103, -67, -100],
                      [90, -24, 103, -67, -115],
                      [90, -20, 72, -100, -115]]
    # 右货仓取出
    def depo_right_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.wait()
