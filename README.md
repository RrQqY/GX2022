# GX2022
2022年大学生工程训练大赛代码库

## ToDo List

- order3（仓库下层抓取）、order4（粗加工区放置）、order5（粗加工区抓取）加速
- 第一次右移到货架前（order3前）由于矫正而卡死
- order8（半成品区上层放置）中间货物放完爪子抽出时会把中间上层物块带倒
- IMU第二圈出现误差
- 进基地、回基地



## Code on Arduino Mega 2560

### 文件组成

- **gx_campus2**

  主程序，存放下位机程序主流程。

- **gpio**

  存放和IO接口有关的函数，以便其他文件直接调用。如start按钮、七路等。

- **move**

  存放和小车底盘运动控制有关的函数。如数线、矫正、转向等，主中断也包含在内。

- **imu**

  存放和IMU有关的函数。如读取yaw角等。

- **utilities**

  其他函数库。如重写的delay等。

- **pi**

  存放和与上位机通信有关的函数。

### 下位机方案

第一趟：

出发时车头向右——向左前方斜向移动2格——直走一格——上位机扫描二维码（无需传回）——直走三格——上位机识别货架颜色——右移至右七路压线——上位机抓取货物①——左移一格——直走一格——左转90度——直走2格——左移到右七路压线——上位机放下货物②——上位机抓取货物③——右移一格——直走两格——左转90度——直走3格——右移至左七路压线——上位机放下货物④——左移一格——左转90度——直走四格——左转90度

第二趟：

直走两格——右移至右七路压线——上位机抓取货物⑤——左移一格——直走一格——左转90度——直走2格——左移到右七路压线——上位机放下货物②——上位机抓取货物③——右移一格——直走两格——左转90度——直走3格——右移至左七路压线——上位机放下货物⑥——左移一格——左转90度——直走两格——向右前方斜向移动2格

### 需要和上位机通信的内容

1. 上位机扫描二维码
2. 上位机识别货架颜色
3. 上位机抓取货物①
4. 上位机放下货物②
5. 上位机抓取货物③
6. 上位机放下货物④
7. 上位机抓取货物⑤
8. 上位机放下货物⑥
