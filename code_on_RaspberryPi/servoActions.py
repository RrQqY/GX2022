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

    # -------- 与货架相关的动作 --------
    # 抓取准备（起始动作），1度
    prepare_1 = [[0 for i in range(5)] for j in range(1)]             
    prepare_1 = [[1, 0, 90, -30, -85]]
    def Servo_prepare_1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare_1[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare_1[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare_1[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare_1[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare_1[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)

    # 抓取准备（起始动作），0度
    prepare_0 = [[0 for i in range(5)] for j in range(1)]             
    prepare_0 = [[0, 0, 90, -30, -85]]
    def Servo_prepare_0(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare_0[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare_0[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare_0[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare_0[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare_0[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.1)

    # 抓取准备（起始动作），0度
    prepare = [[0 for i in range(5)] for j in range(1)]             
    prepare = [[0, 0, 90, -30, -85]]
    def Servo_prepare(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.prepare[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.prepare[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.prepare[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.prepare[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.prepare[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)

    # 抓取货架①（场地下方）上层
    pla1_pos1_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置一
    pla1_pos2_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置二
    pla1_pos3_up_get = [[0 for i in range(5)] for j in range(4)]      # 抓取货架①上层位置三
    pla1_pos1_up_get = [[66, 8, 120, 20, -85],       # 准备
                        [66, -50, 38, 0, -85],       # 伸到物块前
                        [66, -50, 38, 0, -110],      # 抓
                        [66, 8, 80, -70, -110]]      # 抓回到准备位置
    # 抓取货架①（场地下方）上层位置1
    def Get_pla1_pos1_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[1][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[1][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[1][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_up_get[3][1],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_up_get[3][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_up_get[3][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla1_pos2_up_get = [[90, 8, 120, 20, -85],
                        [90, -37, 61, 7, -85],
                        [90, -37, 61, 7, -110],
                        [90, 8, 80, -70, -110]]
    # 抓取货架①（场地下方）上层位置2
    def Get_pla1_pos2_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[1][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[1][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[1][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_up_get[3][1],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_up_get[3][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_up_get[3][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla1_pos3_up_get = [[114, 8, 120, 20, -85],
                        [114, -50, 38, 0, -85],
                        [114, -50, 38, 0, -110],
                        [114, 8, 80, -70, -110]]
    # 抓取货架①（场地下方）上层位置3
    def Get_pla1_pos3_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[0][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[1][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[1][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[1][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_up_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_up_get[3][1],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_up_get[3][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_up_get[3][3],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_up_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 抓取货架①（场地下方）下层
    pla1_pos1_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置一
    pla1_pos2_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置二
    pla1_pos3_down_get = [[0 for i in range(5)] for j in range(4)]    # 抓取货架①下层位置三
    pla1_pos1_down_get = [[65, -40, 122, 70, -85],      # 准备
                          [65, -71, 55, 36, -85],       # 伸到物块前
                          [65, -71, 55, 36, -112],       # 抓
                          [65, -24, 135, 52, -112]]      # 抓回到准备位置
    # 抓取货架①（场地下方）下层位置1
    def Get_pla1_pos1_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[0][1],velocity=30.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[0][2],velocity=50.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[0][3],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[1][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[1][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos1_down_get[3][0],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos1_down_get[3][1],velocity=200.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos1_down_get[3][2],velocity=150.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos1_down_get[3][3],velocity=70.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos1_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla1_pos2_down_get = [[90, -37, 135, 72, -85],
                          [90, -60, 84, 54, -85],
                          [90, -60, 84, 54, -112],
                          [90, -18, 135, 52, -112]]
    # 抓取货架①（场地下方）下层位置2
    def Get_pla1_pos2_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[0][1],velocity=30.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[0][2],velocity=50.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[0][3],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[1][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[1][2],velocity=170.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos2_down_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos2_down_get[3][1],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos2_down_get[3][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos2_down_get[3][3],velocity=70.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos2_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla1_pos3_down_get = [[114, -40, 122, 70, -85],
                          [114, -70, 55, 36, -85],
                          [114, -70, 55, 36, -112],
                          [114, -24, 135, 52, -112]]
    # 抓取货架①（场地下方）下层位置3
    def Get_pla1_pos3_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[0][1],velocity=30.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[0][2],velocity=50.0, t_acc=600, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[0][3],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[1][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[1][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla1_pos3_down_get[3][0],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla1_pos3_down_get[3][1],velocity=200.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla1_pos3_down_get[3][2],velocity=150.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla1_pos3_down_get[3][3],velocity=70.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla1_pos3_down_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 放置货架②（场地右侧）
    pla2_pos1_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置一
    pla2_pos2_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置二
    pla2_pos3_put = [[0 for i in range(5)] for j in range(5)]         # 放置货架②位置三
    pla2_pos1_put = [[65, -5, 82, -30, -115],       # 先把物块移出去
                     [65, -60, 57, 35, -110],       # 放到色环正上方
                     [65, -74, 60, 44, -110],       # 放到色环上
                     [65, -74, 60, 44, -85],        # 松开
                     [65, -40, 121, 70, -85]]       # 缩回
    # 放置货架②（场地右侧）位置1
    def Put_pla2_pos1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[2][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_put[4][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla2_pos2_put = [[91, -5, 82, -30, -115],        # 先把物块移出去
                     [90, -50, 84, 70, -110],
                     [90, -69, 84, 56, -110],
                     [90, -69, 84, 56, -85],
                     [90, -50, 120, 80, -85]]
    # 放置货架②（场地右侧）位置2
    def Put_pla2_pos2(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[2][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_put[4][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla2_pos3_put = [[114, -5, 82, -30, -115],       # 先把物块移出去
                     [114, -60, 57, 35, -110],       # 放到色环正上方
                     [114, -74, 60, 44, -110],       # 放到色环上
                     [114, -74, 60, 44, -85],        # 松开
                     [114, -40, 121, 70, -85]]       # 缩回
    # 放置货架②（场地右侧）位置3
    def Put_pla2_pos3(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[2][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_put[4][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 抓取货架②（场地右侧）
    pla2_pos1_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置一
    pla2_pos2_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置二
    pla2_pos3_get = [[0 for i in range(5)] for j in range(4)]         # 抓取货架②位置三
    pla2_pos1_get = [[65, 0, 82, -30, -85],       # 先把物块移出去
                     [65, -58, 118, 82, -85],       # 准备
                     [65, -77, 56, 44, -85],        # 伸到物块前
                     [65, -77, 56, 44, -112],       # 抓
                     [65, -5, 72, -40, -112]]      # 拎起
    # 抓取货架②（场地右侧）位置1
    def Get_pla2_pos1(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[1][0],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[1][1],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[1][2],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[1][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[2][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[2][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[2][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos1_get[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos1_get[4][1],velocity=200.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos1_get[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos1_get[4][3],velocity=70.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos1_get[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla2_pos2_get = [[90, 0, 82, -30, -85],       # 先把物块移出去
                     [90, -61, 117, 85, -85],
                     [90, -67, 76, 48, -85],
                     [90, -67, 76, 48, -112],
                     [90, -5, 72, -100, -112]] 
    # 抓取货架②（场地右侧）位置2
    def Get_pla2_pos2(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[1][0],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[1][1],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[1][2],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[1][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[2][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[2][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[2][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos2_get[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos2_get[4][1],velocity=200.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos2_get[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos2_get[4][3],velocity=70.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos2_get[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla2_pos3_get = [[114, 0, 82, -30, -85],       # 先把物块移出去
                     [114, -58, 118, 82, -85],       # 准备
                     [114, -77, 56, 44, -85],        # 伸到物块前
                     [114, -77, 56, 44, -112],       # 抓
                     [114, -5, 72, -40, -112]]      # 拎起
    # 抓取货架②（场地右侧）位置3
    def Get_pla2_pos3(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[1][0],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[1][1],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[1][2],velocity=30.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[1][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[2][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[2][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[2][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla2_pos3_get[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla2_pos3_get[4][1],velocity=200.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla2_pos3_get[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla2_pos3_get[4][3],velocity=70.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla2_pos3_get[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 放置货架③（场地上方）下层
    pla3_pos1_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置一
    pla3_pos2_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置二
    pla3_pos3_down_put = [[0 for i in range(5)] for j in range(5)]    # 放置货架③下层位置三
    pla3_pos1_down_put = [[59, -5, 82, -30, -115],       # 先把物块移出去
                          [59, -45, 119, 85, -110],       # 放到色环上方
                          [59, -65, 122, 94, -110],       # 放到色环上
                          [59, -65, 122, 94, -80],        # 松开
                          [59, -39, 120, 70, -80]]        # 缩回
    # 放置货架③（场地上方）下层位置1
    def Put_pla3_pos1_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[1][3],velocity=250.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[2][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_down_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_down_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_down_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_down_put[4][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_down_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla3_pos2_down_put = [[90, -5, 82, -30, -115],       # 先把物块移出去
                          [91, -40, 135, 85, -110],
                          [91, -49, 135, 88, -110],
                          [91, -49, 135, 88, -80],
                          [91, -17, 131, 50, -80]]
    # 放置货架③（场地上方）下层位置2
    def Put_pla3_pos2_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[1][3],velocity=250.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[2][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_down_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_down_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_down_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_down_put[4][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_down_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla3_pos3_down_put = [[125, -5, 82, -30, -115],       # 先把物块移出去
                          [125, -45, 119, 85, -110],
                          [125, -66, 120, 94, -110],
                          [125, -66, 120, 94, -80],
                          [125, -39, 120, 70, -80]]
    # 放置货架③（场地上方）下层位置3
    def Put_pla3_pos3_down(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[1][3],velocity=250.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[2][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_down_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_down_put[4][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_down_put[4][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_down_put[4][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_down_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 放置货架③（场地上方）上层
    pla3_pos1_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置一
    pla3_pos2_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置二
    pla3_pos3_up_put = [[0 for i in range(5)] for j in range(4)]      # 放置货架③上层位置三
    pla3_pos1_up_put = [[60, -5, 82, -30, -115],        # 先把物块移出去
                        [60, -17, 115, 38, -110],       # 放到物块上方
                        [60, -38, 123, 65, -110],       # 放到物块上
                        [60, -38, 123, 65, -80],        # 松开
                        [60, 8, 105, 3, -80]]          # 缩回
    # 放置货架③（场地上方）上层位置1
    def Put_pla3_pos1_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[2][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[2][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos1_up_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos1_up_put[4][1],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos1_up_put[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos1_up_put[4][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos1_up_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla3_pos2_up_put = [[92, -5, 82, -30, -115],        # 先把物块移出去
                        [92, -5, 132, 48, -110],
                        [92, -22, 132, 51, -110],
                        [92, -22, 132, 51, -80],
                        [92, 8, 90, -20, -80]]
    # 放置货架③（场地上方）上层位置2
    def Put_pla3_pos2_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[2][1],velocity=130.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[2][2],velocity=200.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos2_up_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos2_up_put[4][1],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos2_up_put[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos2_up_put[4][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos2_up_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    pla3_pos3_up_put = [[125, -5, 82, -30, -115],        # 先把物块移出去
                        [125, -17, 115, 38, -110],
                        [125, -38, 123, 65, -110],
                        [125, -38, 123, 65, -80],
                        [125, 8, 105, 3, -80]]
    # 放置货架③（场地上方）上层位置3
    def Put_pla3_pos3_up(self):
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[0][1],velocity=80.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[0][3],velocity=100.0, t_acc=50, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[1][0],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[1][2],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[1][3],velocity=250.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(4.2)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[2][1],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[2][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[2][3],velocity=50.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.pla3_pos3_up_put[4][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.pla3_pos3_up_put[4][1],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.pla3_pos3_up_put[4][2],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.pla3_pos3_up_put[4][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.pla3_pos3_up_put[4][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # -------- 与仓库相关的动作 --------
    # 放入
    depo_left_in =   [[0 for i in range(5)] for j in range(4)]      # 放入左货仓
    depo_middle_in = [[0 for i in range(5)] for j in range(4)]      # 放入中货仓
    depo_right_in =  [[0 for i in range(5)] for j in range(4)]      # 放入右货仓
    depo_left_in =   [[-90, -20, 67, -104, -112],       # 移到左仓库上方
                      [-90, -24, 103, -67, -112],       # 移到左仓库内
                      [-90, -24, 103, -67, -85],       # 松开
                      [-90, -20, 67, -104, -85]]       # 抬起到左仓库上方
    
    # 左货仓放入
    def Depo_left_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[0][1],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[0][2],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[0][3],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(2.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    depo_middle_in = [[0, -20, 67, -104, -112],
                      [0, -24, 103, -67, -112],
                      [0, -24, 103, -67, -85],
                      [0, -20, 67, -104, -85]]
    # 中货仓放入
    def Depo_middle_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[0][1],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[0][2],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[0][3],velocity=165.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(2.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    depo_right_in = [[90, -20, 67, -104, -112],
                     [90, -24, 103, -67, -112],
                     [90, -24, 103, -67, -85],
                     [90, -20, 67, -104, -85]]
    # 右货仓放入
    def Depo_right_in(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[0][0],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[0][1],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[0][2],velocity=100.0, t_acc=10, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[0][3],velocity=160.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(2.7)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(0.5)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_in[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_in[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_in[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_in[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_in[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    # 取出
    depo_left_out =   [[0 for i in range(5)] for j in range(4)]      # 拿出左货仓
    depo_middle_out = [[0 for i in range(5)] for j in range(4)]      # 拿出中货仓
    depo_right_out =  [[0 for i in range(5)] for j in range(4)]      # 拿出右货仓
    depo_left_out =   [[-90, -20, 67, -96, -85],       # 移到左仓库上方
                       [-90, -24, 103, -62, -85],       # 移到左仓库内
                       [-90, -24, 103, -62, -115],       # 抓
                       [-90, -20, 67, -96, -115]]       # 抬起到左仓库上方
    # 左货仓取出
    def Depo_left_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_left_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_left_out[3][1],velocity=150.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_left_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_left_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_left_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    depo_middle_out = [[0, -20, 67, -100, -85],
                       [0, -24, 103, -62, -85],
                       [0, -24, 103, -62, -115],
                       [0, -20, 67, -100, -115]]
    # 中货仓取出
    def Depo_middle_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_middle_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_middle_out[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_middle_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_middle_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_middle_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)


    depo_right_out = [[90, -20, 67, -100, -85],
                      [90, -24, 103, -62, -85],
                      [90, -24, 103, -62, -115],
                      [90, -20, 67, -100, -115]]
    # 右货仓取出
    def Depo_right_out(self):
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[0][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[0][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[0][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[0][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[0][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(3)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[1][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[1][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[1][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[1][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[1][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[2][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[2][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[2][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[2][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[2][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
        self.uservo.set_servo_angle(self.SERVO_ID_0, servoActions.depo_right_out[3][0],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_1, servoActions.depo_right_out[3][1],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_2, servoActions.depo_right_out[3][2],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_3, servoActions.depo_right_out[3][3],velocity=100.0, t_acc=100, t_dec=100)
        self.uservo.set_servo_angle(self.SERVO_ID_5, servoActions.depo_right_out[3][4],velocity=100.0, t_acc=100, t_dec=100)
        # self.uservo.wait()
        time.sleep(1)
