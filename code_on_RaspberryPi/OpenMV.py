# openmv：  1）获取二维码、物料放置位置顺序，并串口输出  QRx_XXX/WLx_XXX
#           2）解算机械臂在原料区的抓取顺序，并串口输出       CTx_XXX (X = 1,2,3)
#      是否需要识别色环的顺序？ 即粗加工、半成品区色环的顺序，然后对应放置？
#
#      TIPS:  以原料区为例，有【左-1|中-2|右-3】三个位置放置有物料，对应三个动作组.
#             而所谓抓取顺序，即为机械臂【执行抓取动作组的顺序】。
#             如 312，即为先抓右侧、再抓左侧、最后抓中间。

import sensor, image, time, math, lcd
from pyb import Pin, Timer
from pyb import UART


height = 120
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_windowing(320,240))
sensor.set_auto_gain(False)       # must be turned off for color tracking
sensor.set_auto_whitebal(False)   # must be turned off for color tracking
clock = time.clock()
red_block_x=1
green_block_x=2
blue_block_x=3

# 颜色阈值(L Min, L Max, A Min, A Max, B Min, B Max)
thresholds = [(0, 83, 22, 127, -128, 127),      # 红色阈值
              (13, 93, -128, -20, -128, 127),    # 绿色阈值
              (0, 100, -20, 126, -128, -7)]     # 蓝色阈值

#################### Openmv数据处理 ###################
# 直接向arduino发送处理好的数据
# 红-1 绿-2 蓝-3

# 需要获取的顺序
Aorder=0          # 上层物料放置顺序
Border=0          # 下层物料放置顺序

Pos1 = "000"      # 上层放置位置
Pos2 = "000"      # 下层放置位置

def find_min(blobs):
    min_size=1000000
    for blob in blobs:
        if blob[2]*blob[3] <= min_size:
            min_blob=blob
            min_size = blob[2]*blob[3]
    return min_blob

# 与arduino Mega串口通信

uart = UART(3, 9600, timeout_char = 50)   # 串口3 [TX-P4, RX-P5]

# 串口收发数据
recv_data = ""     # 串口接收的数据 【 CM+QR|扫描二维码、CM+WL|
WL_flag = 0        # 获取上层物料放置顺序标志位


# 串口发送物料位置   WL1_XXX\WL2_XXX

# 串口接收数据
def Uart_recv():
    global WL_flag

    if (uart.any()):   # 更新串口接收数据
        recv_data = eval(str(uart.read()))

        print(recv_data)

        if ("WL" in recv_data):
            WL_flag = 1
            print("Ready for WLpose task !")


# 主循环
while(True):
    clock.tick()
    img = sensor.snapshot()

    Uart_recv() # 串口接收（接收arduino发送的指令）

    if(WL_flag): # 识别物料    WL_flag
        clock.tick()
        light = Timer(2, freq=50000).channel(1, Timer.PWM, pin=Pin("P6"))
        light.pulse_width_percent(100) # 控制亮度 0~100

        img = sensor.snapshot()

        # 识别下层物料顺序
        for r in img.find_blobs([thresholds[0]],roi=[0,140,320,100],pixels_threshold=200, area_threshold=200, merge=True):
            img.draw_rectangle(r.rect())
            img.draw_cross(r.cx(), r.cy())
            img.draw_keypoints([(r.cx(), r.cy(), int(math.degrees(r.rotation())))], size=20)
            red_block_x = r.cx()

        for g in img.find_blobs([thresholds[1]],roi=[0,140,320,100], pixels_threshold=200, area_threshold=200, merge=True):
            img.draw_rectangle(g.rect())
            img.draw_cross(g.cx(), g.cy())
            img.draw_keypoints([(g.cx(), g.cy(), int(math.degrees(g.rotation())))], size=20)
            green_block_x = g.cx()

        for b in img.find_blobs([thresholds[2]],roi=[0,140,320,100], pixels_threshold=200, area_threshold=200, merge=True):
            img.draw_rectangle(b.rect())
            img.draw_cross(b.cx(), b.cy())
            img.draw_keypoints([(b.cx(), b.cy(), int(math.degrees(b.rotation())))], size=20)
            blue_block_x = b.cx()

            if int(red_block_x)<int(green_block_x) and int(green_block_x)<int(blue_block_x):
                if Border!=123:
                    #print("上层物料顺序为：红绿蓝")
                    #print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=123
            elif int(blue_block_x)<int(green_block_x) and int(green_block_x)<int(red_block_x):
                if Border!=321:
                    #print("上层物料顺序为：蓝绿红")
                    #print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=321
            elif int(red_block_x)<int(blue_block_x) and int(blue_block_x)<int(green_block_x):
                if Border!=132:
                    #print("上层物料顺序为：红蓝绿")
                    #print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=132
            elif int(green_block_x)<int(blue_block_x) and int(blue_block_x)<int(red_block_x):
                if Border!=231:
                    #print("上层物料顺序为：绿蓝红")
                    # print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=231
            elif int(blue_block_x)<int(red_block_x) and int(red_block_x)<int(green_block_x):
                if Border!=312:
                    #print("上层物料顺序为：蓝红绿")
                    #print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=312
            elif int(green_block_x)<int(red_block_x) and int(red_block_x)<int(blue_block_x):
                if Border!=213:
                    #print("上层物料顺序为：绿红蓝")
                    #print(red_block_x,green_block_x,blue_block_x)
                    #print(blob.h(),blob.w() )
                    Border=213

            # 识别上层物料顺序
            if (Border==123) or (Border==132) or (Border==213) or (Border==231) or (Border==312) or (Border==321):
                for r in img.find_blobs([thresholds[0]],roi=[0,0,320,100],pixels_threshold=200, area_threshold=200, merge=True):
                    img.draw_rectangle(r.rect())
                    img.draw_cross(r.cx(), r.cy())
                    img.draw_keypoints([(r.cx(), r.cy(), int(math.degrees(r.rotation())))], size=20)
                    red_block_x = r.cx()

                for g in img.find_blobs([thresholds[1]],roi=[0,0,320,100], pixels_threshold=200, area_threshold=200, merge=True):
                    img.draw_rectangle(g.rect())
                    img.draw_cross(g.cx(), g.cy())
                    img.draw_keypoints([(g.cx(), g.cy(), int(math.degrees(g.rotation())))], size=20)
                    green_block_x = g.cx()

                for b in img.find_blobs([thresholds[2]],roi=[0,0,320,100], pixels_threshold=200, area_threshold=200, merge=True):
                    img.draw_rectangle(b.rect())
                    img.draw_cross(b.cx(), b.cy())
                    img.draw_keypoints([(b.cx(), b.cy(), int(math.degrees(b.rotation())))], size=20)
                    blue_block_x = b.cx()

                    if int(red_block_x)<int(green_block_x) and int(green_block_x)<int(blue_block_x):
                        if Aorder!=123:
                            #print("上层物料顺序为：红绿蓝")
                            #print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=123
                    elif int(blue_block_x)<int(green_block_x) and int(green_block_x)<int(red_block_x):
                        if Aorder!=321:
                            #print("上层物料顺序为：蓝绿红")
                            #print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=321
                    elif int(red_block_x)<int(blue_block_x) and int(blue_block_x)<int(green_block_x):
                        if Aorder!=132:
                            #print("上层物料顺序为：红蓝绿")
                            #print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=132
                    elif int(green_block_x)<int(blue_block_x) and int(blue_block_x)<int(red_block_x):
                        if Aorder!=231:
                            #print("上层物料顺序为：绿蓝红")
                            # print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=231
                    elif int(blue_block_x)<int(red_block_x) and int(red_block_x)<int(green_block_x):
                        if Aorder!=312:
                            #print("上层物料顺序为：蓝红绿")
                            #print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=312
                    elif int(green_block_x)<int(red_block_x) and int(red_block_x)<int(blue_block_x):
                        if Aorder!=213:
                            #print("上层物料顺序为：绿红蓝")
                            #print(red_block_x,green_block_x,blue_block_x)
                            #print(blob.h(),blob.w() )
                            Aorder=213


                    print("%dand%d"%(int(Aorder),int(Border)))
                    if int(Aorder)!= 0 and int(Border)!=0 :
                        print("OK!")

                        Pos1 = str(Aorder)
                        Pos2 = str(Border)

                        # 当物料识别成功后 【处理数据，发送数据】
                        print("WL_"+Pos1+Pos2)
                        uart.write("WL_"+Pos1+Pos2+"\r\n")

                        WL_flag = 0
                        print("Done! ")
                        light.pulse_width_percent(0)
