#coding:utf-8

from __future__ import absolute_import
from uservo import UartServoManager
import time
import serial
import cv2
import numpy as np
import struct
import sys
import servoActions as sa
import RPi.GPIO as GPIO

sys.path.append(u"../../src")      # 添加uservo.py的系统路径

global target_up          # 上层抓取目标顺序
global target_down        # 下层抓取目标顺序
global seq_up             # 上层摆放目标顺序
global seq_down           # 下层摆放目标顺序

global turnCount          # 当前执行轮数


# 初始化所有串口
# -------- 与下位机Mega通信串口配置 --------
# 参数配置
Mega_PORT_NAME =  "/dev/ttyS0"		    # 串口号
Mega_BAUDRATE  =  115200			    # 波特率

# 初始化串口
Mega_uart = serial.Serial(port=Mega_PORT_NAME, baudrate=Mega_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

# -------- 与GM65模块通信串口配置 --------
# 参数配置
GM65_PORT_NAME =  "/dev/ttyAMA1"		# 串口号
GM65_BAUDRATE  = 9600			        # 波特率

# 初始化串口
GM65_uart = serial.Serial(port=GM65_PORT_NAME, baudrate=GM65_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

# -------- 与LCD屏通信串口配置 --------
# 参数配置
LCD_PORT_NAME =  "/dev/ttyAMA3"		# 串口号
LCD_BAUDRATE  =  115200			    # 波特率

# 初始化串口
LCD_uart = serial.Serial(port=LCD_PORT_NAME, baudrate=LCD_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

# -------- 与OpenMV通信串口配置 --------
# 参数配置
OPENMV_PORT_NAME =  "/dev/ttyAMA2"		# 串口号
OPENMV_BAUDRATE  =  9600			    # 波特率

# 初始化串口
OPENMV_uart = serial.Serial(port=OPENMV_PORT_NAME, baudrate=OPENMV_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

# -------- 与舵机通信串口配置 --------
# # 参数配置
# SERVO_PORT_NAME =  u'/dev/ttyUSB0'		# 舵机串口号
# SERVO_BAUDRATE = 115200			        # 舵机的波特率
# SERVO_ID_0 = 0					        # 舵机的ID号
# SERVO_ID_1 = 1
# SERVO_ID_2 = 2
# SERVO_ID_3 = 3
# SERVO_ID_5 = 5
# SERVO_HAS_MTURN_FUNC = False	        # 舵机是否拥有多圈模式

# # 初始化串口
# servo_uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
#                     parity=serial.PARITY_NONE, stopbits=1,\
#                     bytesize=8,timeout=0)
# # 初始化舵机管理器
# uservo = UartServoManager(servo_uart, is_debug=True)
servo = sa.servoActions()

lightPin = 5
GPIO.setmode(GPIO.BOARD)        # BMC或者BOARD模式
GPIO.setup(lightPin, GPIO.OUT)


# 从下位机获取当前需执行的任务编号
def get_order():
    recv = ''
    # 获得接收缓冲区字符
    count = Mega_uart.inWaiting()
    if count != 0:
        # 读取内容
        recv = Mega_uart.read(count)  #树莓派串口接收数据
    # 清空接收缓冲区
    Mega_uart.flushInput()

    # 任务0：开始程序
    if recv == '0':
        order = 0
        print('@ Get order , start game!')
        time.sleep(0.01)
        return order
    # 任务1：扫描二维码
    elif recv == '1':
        order = 1
        print('@ Get order 1')
        time.sleep(0.01)
        return order
    # 任务2：识别货架颜色
    elif recv == '2':
        order = 2
        print('@ Get order 2')
        time.sleep(0.01)
        return order
    # 任务3：抓取货物①（场地下方）上层位置
    elif recv == '3':
        order = 3
        print('@ Get order 3')
        time.sleep(0.01)
        return order
    # 任务4：放下货物②（场地右侧）位置
    elif recv == '4':
        order = 4
        print('@ Get order 4')
        time.sleep(0.01)
        return order
    # 任务5：抓取货物③（场地右侧）位置
    elif recv == '5':
        order = 5
        print('@ Get order 5')
        time.sleep(0.01)
        return order
    # 任务6：放下货物④（场地上方）下层位置
    elif recv == '6':
        order = 6
        print('@ Get order 6')
        time.sleep(0.01)
        return order
    # 任务7：抓取货物⑤（场地下方）下层位置
    elif recv == '7':
        order = 7
        print('@ Get order 7')
        time.sleep(0.01)
        return order
    # 任务8：抓取货物⑥（场地上方）上层位置
    elif recv == '8':
        order = 8
        print('@ Get order 8')
        time.sleep(0.01)
        return order
    # 任务9：结束回基地时爪子折叠
    elif recv == '9':
        order = 9
        print('@ Get order 9')
        time.sleep(0.01)
        return order


# 任务1：扫描二维码
def order1():
    print("@ Start order 1")

    start = '7e000801000201abcd'
    start_hex = start.decode('hex')
    recv = ''
    target_up = 0
    target_down = 0
    target_up_str = ''
    target_down_str = ''

    timeStart = time.time()

    while True:
        # 发送拍摄开始数据段
        GM65_uart.write(start_hex)
        # 获得接收缓冲区字符
        count = GM65_uart.inWaiting()
        if count != 0:
            recv = GM65_uart.read(count)       # 树莓派串口接收数据
        if '+' in recv:
            pos = recv.find('+')
            target_up_str = recv[pos-3 : pos]
            target_down_str = recv[pos+1 : pos+4]
            target_up = int(target_up_str)
            target_down = int(target_down_str)
            print('@ Get target: ', target_up, target_down)
            break;
        else :
            timeNow = time.time()
            if timeNow - timeStart > 1.5:
                print('@ Time 1 out')
                break;
        
        # 清空接收缓冲区
        GM65_uart.flushInput()
        # 必要的软件延时
        time.sleep(0.1)

    LCD_print(target_up, target_down)
    return target_up, target_down


# 任务2：识别货架颜色
def order2():
    print("@ Start order 2")

    recv = ''
    seq_up = 0
    seq_down = 0
    seq_up_str = ''
    seq_down_str = ''
    seq_up_old = 0
    seq_down_old = 0

    timeStart = time.time()

    start_flag = "WL"
    time.sleep(0.2)
    # OPENMV_uart.write(start_flag.encode('utf-8'))

    while True:
        # 向OpenMV发送开始识别信号
        OPENMV_uart.write(start_flag.encode('utf-8'))

        # 获得接收缓冲区字符
        count = OPENMV_uart.inWaiting()
        if count != 0:
            recv = OPENMV_uart.read(count)    # 树莓派串口接收数据
            if 'WL_' in recv:
                pos = recv.find('_')
                seq_up_str = recv[pos + 1 : pos + 4]
                seq_down_str = recv[pos + 4 : pos + 7]
                seq_up = int(seq_up_str)
                seq_down = int(seq_down_str)

                print('@ Get color sequence: ', seq_up, seq_down)

                # 检测两次识别结果是否一致，如果一致才返回
                if (seq_up_old == seq_up) and (seq_down_old == seq_down):
                    print('@ Color sequence is the same')
                    break
                else:
                    seq_up_old = seq_up
                    seq_down_old = seq_down
            else:
                timeNow = time.time()
                if timeNow - timeStart > 1.5:
                    print('@ Time 2 out')
                    break

        # 清空接收缓冲区
        OPENMV_uart.flushInput()
        # 必要的软件延时
        time.sleep(0.1)

    print('@ Return color sequence: ', seq_up, seq_down)
    return seq_up, seq_down


# 在场地下方货架处抓取货物后判断其颜色，并放到指定仓库（上层）
def judge_color_up(target_up, pos):
    target_up_str = str(target_up)
    res = target_up_str[pos - 1]
    if res == '1':        # 红色
        depo_flag = str(pos) + 'to1'
        # print('@@',depo_flag)
        servo.Depo_right_in(depo_flag)
    elif res == '2':      # 绿色
        depo_flag = str(pos) + 'to2'
        servo.Depo_middle_in(depo_flag)
    elif res == '3':      # 蓝色
        depo_flag = str(pos) + 'to3'
        servo.Depo_left_in(depo_flag)

# 在场地下方货架处抓取货物后判断其颜色，并放到指定仓库（下层）
def judge_color_down(target_down, pos):
    target_down_str = str(target_down)
    res = target_down_str[pos - 1]
    if res == '1':        # 红色
        depo_flag = str(pos) + 'to1'
        servo.Depo_right_in(depo_flag)
    elif res == '2':      # 绿色
        depo_flag = str(pos) + 'to2'
        servo.Depo_middle_in(depo_flag)
    elif res == '3':      # 蓝色
        depo_flag = str(pos) + 'to3'
        servo.Depo_left_in(depo_flag)


def getGraspSeq(seq, target):
    grasp_seq = []
    target_str = str(target)
    seq_str = str(seq)
    for i in target_str:
        i_int = int(i)
        grasp_seq.append(str(seq_str.index(str(i_int)) + 1))
        grasp_str = ''.join(grasp_seq)
    return int(grasp_str)


# 任务3：抓取货物①（场地下方）上层位置
def order3(seq_up, target_up):
    print("@ Start order 3")
    grasp_seq_up = getGraspSeq(seq_up, target_up)
    if grasp_seq_up == 123:
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
    if grasp_seq_up == 132:
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
    if grasp_seq_up == 213:
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
    if grasp_seq_up == 231:
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)
    if grasp_seq_up == 312:
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
    if grasp_seq_up == 321:
        servo.Get_pla1_pos3_up()
        judge_color_up(seq_up, 3)
        servo.Get_pla1_pos2_up()
        judge_color_up(seq_up, 2)
        servo.Get_pla1_pos1_up()
        judge_color_up(seq_up, 1)


# 任务4：放下货物②（场地右侧）位置
def order4(target):
    print("@ Start order 4")
    # 从右往左放置（红绿蓝）
    if target == 321:    
        servo.Depo_left_out('0to0')
        servo.Put_pla2_pos1('3to1')
        servo.Depo_middle_out('2to2')
        servo.Put_pla2_pos2('2to2')
        servo.Depo_right_out('2to1')
        servo.Put_pla2_pos3('1to3')
    elif target == 312:
        servo.Depo_left_out('0to0')
        servo.Put_pla2_pos1('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla2_pos3('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla2_pos2('2to2')
    elif target == 231:
        servo.Depo_middle_out('0to0')
        servo.Put_pla2_pos2('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla2_pos1('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla2_pos3('1to3')
    elif target == 213:
        servo.Depo_middle_out('0to0')
        servo.Put_pla2_pos2('2to2')
        servo.Depo_right_out('2to1')
        servo.Put_pla2_pos3('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla2_pos1('3to1')
    elif target == 132:
        servo.Depo_right_out('0to0')
        servo.Put_pla2_pos3('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla2_pos1('3to1')
        servo.Depo_middle_out('1to2')
        servo.Put_pla2_pos2('2to2')
    elif target == 123:
        servo.Depo_right_out('0to0')
        servo.Put_pla2_pos3('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla2_pos2('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla2_pos1('3to1')


# 任务5：抓取货物③（场地右侧）位置
def order5(target):
    print("@ Start order 5")
    # 从左往右抓取（蓝绿红）
    if target == 321:    
        servo.Get_pla2_pos1('0to0')
        servo.Depo_left_in('1to3')
        servo.Get_pla2_pos2('3to2')
        servo.Depo_middle_in('2to2')
        servo.Get_pla2_pos3('2to3')
        servo.Depo_right_in('3to1')
    elif target == 312:
        servo.Get_pla2_pos1('0to0')
        servo.Depo_left_in('1to3')
        servo.Get_pla2_pos3('3to3')
        servo.Depo_right_in('3to1')
        servo.Get_pla2_pos2('1to2')
        servo.Depo_middle_in('2to2')
    elif target == 231:
        servo.Get_pla2_pos2('0to0')
        servo.Depo_middle_in('2to2')
        servo.Get_pla2_pos1('2to1')
        servo.Depo_left_in('1to3')
        servo.Get_pla2_pos3('3to3')
        servo.Depo_right_in('3to1')
    elif target == 213:
        servo.Get_pla2_pos2('0to0')
        servo.Depo_middle_in('2to2')
        servo.Get_pla2_pos3('2to3')
        servo.Depo_right_in('3to1')
        servo.Get_pla2_pos1('1to1')
        servo.Depo_left_in('1to3')
    elif target == 132:
        servo.Get_pla2_pos3('0to0')
        servo.Depo_right_in('3to1')
        servo.Get_pla2_pos1('1to1')
        servo.Depo_left_in('1to3')
        servo.Get_pla2_pos2('3to2')
        servo.Depo_middle_in('2to2')
    elif target == 123:
        servo.Get_pla2_pos3('0to0')
        servo.Depo_right_in('3to1')
        servo.Get_pla2_pos2('1to2')
        servo.Depo_middle_in('2to2')
        servo.Get_pla2_pos1('2to1')
        servo.Depo_left_in('1to3')


# 任务6：放下货物④（场地上方）下层位置
def order6(target_up):
    print("@ Start order 6")
    if target_up == 321:
        servo.Depo_left_out('0to0')
        servo.Put_pla3_pos1_down('3to1')
        servo.Depo_middle_out('1to2')
        servo.Put_pla3_pos2_down('2to2')    
        servo.Depo_right_out('2to1')
        servo.Put_pla3_pos3_down('1to3')
    elif target_up == 312:
        servo.Depo_left_out('0to0')
        servo.Put_pla3_pos1_down('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla3_pos3_down('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla3_pos2_down('2to2')
    elif target_up == 231:
        servo.Depo_middle_out('0to0')
        servo.Put_pla3_pos2_down('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla3_pos1_down('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla3_pos3_down('1to3')
    elif target_up == 213:
        servo.Depo_middle_out('0to0')
        servo.Put_pla3_pos2_down('2to2')
        servo.Depo_right_out('2to1')
        servo.Put_pla3_pos3_down('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla3_pos1_down('3to1')
    elif target_up == 132:
        servo.Depo_right_out('0to0')
        servo.Put_pla3_pos3_down('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla3_pos1_down('3to1')
        servo.Depo_middle_out('1to2')
        servo.Put_pla3_pos2_down('2to2')
    elif target_up == 123:
        servo.Depo_right_out('0to0')
        servo.Put_pla3_pos3_down('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla3_pos2_down('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla3_pos1_down('3to1')


# 任务7：抓取货物⑤（场地下方）下层位置
def order7(seq_down, target_down):
    print("@ Start order 7")
    grasp_seq_down = getGraspSeq(seq_down, target_down)
    if grasp_seq_down == 123:
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
    if grasp_seq_down == 132:
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
    if grasp_seq_down == 213:
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
    if grasp_seq_down == 231:
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)
    if grasp_seq_down == 312:
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
    if grasp_seq_down == 321:
        servo.Get_pla1_pos3_down()
        judge_color_down(seq_down, 3)
        servo.Get_pla1_pos2_down()
        judge_color_down(seq_down, 2)
        servo.Get_pla1_pos1_down()
        judge_color_down(seq_down, 1)


# 任务8：抓取货物⑥（场地上方）上层位置
def order8(target_down):
    print("@ Start order 8")
    if target_down == 321:    
        servo.Depo_left_out('0to0')
        servo.Put_pla3_pos1_up('3to1')
        servo.Depo_middle_out('1to2')
        servo.Put_pla3_pos2_up('2to2')
        servo.Depo_right_out('2to1')
        servo.Put_pla3_pos3_up('1to3')
    elif target_down == 312:
        servo.Depo_left_out('0to0')
        servo.Put_pla3_pos1_up('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla3_pos3_up('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla3_pos2_up('2to2')
    elif target_down == 231:
        servo.Depo_middle_out('0to0')
        servo.Put_pla3_pos2_up('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla3_pos1_up('3to1')
        servo.Depo_right_out('1to1')
        servo.Put_pla3_pos3_up('1to3')
    elif target_down == 213:
        servo.Depo_middle_out('0to0')
        servo.Put_pla3_pos2_up('2to2')
        servo.Depo_right_out('2to1')
        servo.Put_pla3_pos3_up('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla3_pos1_up('3to1')
    elif target_down == 132:
        servo.Depo_right_out('0to0')
        servo.Put_pla3_pos3_up('1to3')
        servo.Depo_left_out('3to3')
        servo.Put_pla3_pos1_up('3to1')
        servo.Depo_middle_out('1to2')
        servo.Put_pla3_pos2_up('2to2')
    elif target_down == 123:
        servo.Depo_right_out('0to0')
        servo.Put_pla3_pos3_up('1to3')
        servo.Depo_middle_out('3to2')
        servo.Put_pla3_pos2_up('2to2')
        servo.Depo_left_out('2to3')
        servo.Put_pla3_pos1_up('3to1')


def main():
    turnCount = 1                           # 当前为第几回合

    GPIO.output(lightPin, GPIO.LOW)         # 关闭补光灯
    servo.Servo_start()

    while True:
        # 从下位机获取指令
        order = get_order()

        # order = 2
        # seq_up = 321
        # seq_down = 213
        # target_up = 213
        # target_down = 132

        # 开始执行指令（拍摄）
        if order == 0:
            servo.Servo_start()
        elif order == 1:
            target_up, target_down = order1()
        elif order == 2:
            GPIO.output(lightPin, GPIO.HIGH)        # 打开补光灯
            time.sleep(1)
            servo.Servo_prepare_0()
            seq_up, seq_down = order2()
            GPIO.output(lightPin, GPIO.LOW)         # 关闭补光灯
        elif order == 3:
            order3(seq_up, target_up)
            servo.Servo_prepare()
        elif order == 4:
            if turnCount == 1:
                order4(target_up)
            elif turnCount == 2:
                order4(target_down)
            servo.Servo_prepare()
        elif order == 5:
            if turnCount == 1:
                order5(target_up)
                turnCount = turnCount + 1
            elif turnCount == 2:
                order5(target_down)
            servo.Servo_prepare()
        elif order == 6:
            order6(target_up)
            servo.Servo_prepare()
        elif order == 7:
            order7(seq_down, target_down)
            servo.Servo_prepare()
        elif order == 8:
            order8(target_down)
            servo.Servo_end_out()
            time.sleep(1.5)
            servo.Servo_prepare()
        elif order == 9:
            servo.Servo_start()

        # 必要的软件延时
        time.sleep(0.1)


def LCD_print(target_up, target_down):
    print_s = "CLR(0);SBC(3);DIR(1);DC48(5,5,'UP_TAR:',15);DC48(240,5,'" + str(target_up) + "',15);DC48(5,60,'DOWN_TAR:',15);DC48(240,60,'" + \
                str(target_down) + "',15);PL(0,120,320,120,15);\r\n"
    LCD_uart.write(print_s)


if __name__=='__main__':
    print("@ Start !!!")
    main()