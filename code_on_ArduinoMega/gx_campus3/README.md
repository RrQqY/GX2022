# Code on Arduino Mega 2560

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

