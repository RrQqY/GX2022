#coding:utf-8

import time
import serial

# 参数配置
OPENMV_PORT_NAME =  "/dev/ttyAMA3"		# 串口号
OPENMV_BAUDRATE  =  9600			    # 波特率

# 初始化串口
OPENMV_uart = serial.Serial(port=OPENMV_PORT_NAME, baudrate=OPENMV_BAUDRATE,\
                        parity=serial.PARITY_NONE, stopbits=1,\
                        bytesize=8,timeout=0)

recv = ''

send = "WL"
OPENMV_uart.write(send.encode('utf-8'))

while True:
    # 获得接收缓冲区字符
    count = OPENMV_uart.inWaiting()
    if count != 0:
        # 读取内容并回显
        recv = OPENMV_uart.read(count)  #树莓派串口接收数据
        
        print(recv)
        break

    # 清空接收缓冲区
    OPENMV_uart.flushInput()
    # 必要的软件延时
    time.sleep(0.1)