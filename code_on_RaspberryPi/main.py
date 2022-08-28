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

sys.path.append(u"../../src")      # 添加uservo.py的系统路径

global target_up          # 上层抓取目标顺序
global target_down        # 下层抓取目标顺序
global seq_up             # 上层摆放目标顺序
global seq_down           # 下层摆放目标顺序


# 初始化所有串口
# -------- 与下位机Mega通信串口配置 --------
# 参数配置
Mega_PORT_NAME =  "/dev/ttyS0"		# 串口号
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

# -------- 与OpenMV通信串口配置 --------
# 参数配置
OPENMV_PORT_NAME =  "/dev/ttyAMA3"		# 串口号
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

    if recv == '1':
        order = 1
        print('@ Get order 1')
        time.sleep(0.01)
        return order
    elif recv == '2':
        order = 2
        print('@ Get order 2')
        time.sleep(0.01)
        return order
    elif recv == '3':
        order = 3
        print('@ Get order 3')
        time.sleep(0.01)
        return order
    elif recv == '4':
        order = 4
        print('@ Get order 4')
        time.sleep(0.01)
        return order
    elif recv == '5':
        order = 25
        print('@ Get order 5')
        time.sleep(0.01)
        return order
    elif recv == '6':
        order = 6
        print('@ Get order 6')
        time.sleep(0.01)
        return order
    elif recv == '7':
        order = 7
        print('@ Get order 7')
        time.sleep(0.01)
        return order


# 任务1：扫描二维码
def order1():
    print("@ Start order 1")

    start = '7e000801000201abcd'
    start_hex = start.decode('hex')
    recv = ''
    target_up_str = ''
    target_down_str = ''

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
        
        # 清空接收缓冲区
        GM65_uart.flushInput()
        # 必要的软件延时
        time.sleep(0.1)


# 任务2：识别货架颜色
def order2():
    print("@ Start order 2")

    recv = ''
    start_flag = "WL"
    OPENMV_uart.write(start_flag.encode('utf-8'))

    while True:
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
                break;
            
            break

        # 清空接收缓冲区
        OPENMV_uart.flushInput()
        # 必要的软件延时
        time.sleep(0.1)


# 任务3：抓取货物①
def order3():
    print("@ Start order 3")
    servo.depo_left_out()


# 任务4：放下货物②
def order4():
    print("@ Start order 4")


# 任务5：抓取货物③
def order5():
    print("@ Start order 5")


# 任务6：放下货物④
def order6():
    print("@ Start order 6")


# 任务7：抓取货物⑤
def order7():
    print("@ Start order 7")

# 任务8：抓取货物⑥
def order8():
    print("@ Start order 8")



if __name__=='__main__':
    while True:
        # 从下位机获取指令
        order = get_order()

        # 开始执行指令
        if order == 1:
            order1()
        elif order == 2:
            order2()
        elif order == 3:
            order3()
        elif order == 4:
            order4()
        elif order == 5:
            order5()
        elif order == 6:
            order6()
        elif order == 7:
            order7()

        # 必要的软件延时
        time.sleep(0.1)
