#coding:utf-8

import time
import serial

# 参数配置
Mega_PORT_NAME =  "/dev/ttyS0"		# 串口号
Mega_BAUDRATE  =  115200			    # 波特率

# 初始化串口
Mega_uart = serial.Serial(port=Mega_PORT_NAME, baudrate=Mega_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

recv = ''

while True:
    # 获得接收缓冲区字符
    count = Mega_uart.inWaiting()
    if count != 0:
        # 读取内容并回显
        recv = Mega_uart.read(count)  #树莓派串口接收数据
    # 清空接收缓冲区
    Mega_uart.flushInput()

    if recv == '1':
        print('yesss!')
        break;

    # 必要的软件延时
    time.sleep(0.1)