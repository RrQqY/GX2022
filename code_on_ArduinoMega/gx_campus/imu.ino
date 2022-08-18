/* 这里存储一些和IMU有关的函数 */
#include "gx_campus.h"

// MPU6050 测试例程 请先安装库 https://github.com/jrowberg/i2cdevlib
#include "I2Cdev.h"                          //i2cdevlib/Arduino/I2Cdev/
#include "MPU6050_6Axis_MotionApps612.h"  //i2cdevlib/Arduino/MPU6050/
// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif

MPU6050  mpu;

// MPU control/status vars
bool dmpReady = false;   // set true if DMP init was successful如果dmp设置为真则设置为true
uint8_t mpuIntStatus;    // holds actual interrupt status byte from MPU
uint8_t devStatus;       // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;     // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;      // count of all bytes currently in FIFO
uint8_t fifoBuffer[64];  // FIFO storage buffer FIFO存储缓存区

// orientation/motion vars
Quaternion q;            // [w, x, y, z]    quaternion container
VectorInt16 aa;          // [x, y, z]       accel sensor measurements
VectorInt16 gy;          // [x, y, z]       gyro sensor measurements
VectorInt16 aaReal;      // [x, y, z]       gravity-free accel sensor measurements
VectorInt16 aaWorld;     // [x, y, z]       world-frame accel sensor measurements
VectorFloat gravity;     // [x, y, z]       gravity vector
float       ypr[3];      // [yaw, pitch, roll]    yaw/pitch/roll container and gravity vector


// IMU初始化
void imu_setup() {
  // join I2C bus (I2Cdev library doesn't do this automatically)
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    Wire.begin();
    Wire.setClock(400000);  // 400kHz I2C clock. Comment this line if having
                            // compilation difficulties
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
    Fastwire::setup(400, true);
  #endif

  // NOTE: 8MHz or slower host processors, like the Teensy @ 3.3V or Arduino
  // Pro Mini running at 3.3V, cannot handle this baud rate reliably due to
  // the baud timing being too misaligned with processor ticks. You must use
  // 38400 or slower in these cases, or use some kind of external separate
  // crystal solution for the UART timer.

  // initialize device
  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();

  // verify connection
  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful")
                                      : F("MPU6050 connection failed"));

  // load and configure the DMP
  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();

  //提供陀螺仪的偏移量，运行IMU_Zero获得,按最小灵敏度进行缩放
  mpu.setXAccelOffset(-1664);
  mpu.setYAccelOffset(-5078);
  mpu.setZAccelOffset(831);
  mpu.setXGyroOffset(-37);
  mpu.setYGyroOffset(15);
  mpu.setZGyroOffset(2);        // yaw角的零偏，调这个
  
  // make sure it worked (returns 0 if so)
  if (devStatus == 0) {
    // Calibration Time: generate offsets and calibrate our MPU6050
    mpu.CalibrateAccel(6);
    mpu.CalibrateGyro(6);
    Serial.println();
    mpu.PrintActiveOffsets();
    // turn on the DMP, now that it's ready
    Serial.println(F("Enabling DMP..."));
    mpu.setDMPEnabled(true);

    dmpReady = true;

    // get expected DMP packet size for later comparison
    packetSize = mpu.dmpGetFIFOPacketSize();
  } else {
    // ERROR!
    // 1 = initial memory load failed
    // 2 = DMP configuration updates failed
    // (if it's going to break, usually the code will be 1)
    Serial.print(F("DMP Initialization failed (code "));
    Serial.print(devStatus);
    Serial.println(F(")"));
  }
}

// IMU获取yaw角数据
float get_yaw(){
    // read a packet from FIFO
    if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) {
      mpu.dmpGetQuaternion(&q, fifoBuffer);
      mpu.dmpGetGravity(&gravity, &q);
      mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
      
      return (ypr[0] * 180 / M_PI);
    }
}
