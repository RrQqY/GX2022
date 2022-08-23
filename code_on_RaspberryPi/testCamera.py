#coding:utf-8

import cv2
import numpy as np

ball_color = 'red'

color_dist = {'red': {'Lower': np.array([0, 50, 50]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              }


cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_AUTOSIZE)

# 设置SimpleBlobDetector参数
params = cv2.SimpleBlobDetector_Params()

# 改变阈值
params.minThreshold = 10
params.maxThreshold = 200

params.filterByColor = True


# 根据面积过滤
params.filterByArea = True
params.minArea = 500

# 根据Circularity过滤
params.filterByCircularity = True
params.minCircularity = 0.1

# 根据Convexity过滤
params.filterByConvexity = True
params.minConvexity = 0.87

# 根据Inertia过滤
params.filterByInertia = True
params.minInertiaRatio = 0.01

# 创建一个带有参数的检测器
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


while cap.isOpened():
    ret, frame = cap.read()
    if frame is not None:
        # gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
        # hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                   # 转化成HSV图像
        # erode_hsv = cv2.erode(hsv, None, iterations=2)                    # 腐蚀，粗的变细
        # inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
        # contours, hierarchy = cv2.findContours(inRange_hsv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(inRange_hsv,contours,-1,(0,0,255),10)  

        # cv2.imshow('camera', inRange_hsv)
        # cv2.waitKey(1)


        # 检测blobs
        keypoints = detector.detect(frame)

        # 用红色圆圈画出检测到的blobs
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 确保圆的大小对应于blob的大小
        im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # 结果显示
        cv2.imshow("Keypoints", im_with_keypoints)
        cv2.waitKey(1)

    else:
        print("无画面")
 
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()




