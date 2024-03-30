import numpy as np
import cv2 as cv
cap = cv.VideoCapture("./sources/v1.mp4") #打开一个视频流，涉嫌头或者视频文件
if not cap.isOpened(): 
    print("Cannot open camera")
    exit()
#保存视频
fourcc = cv.VideoWriter_fourcc(*'XVID')  #创建保存视频文件的格式
out = cv.VideoWriter('./soueces/output.avi', fourcc, 20.0, (640,  480)) #（【保存名称】，【格式】，【帧速率】，【帧大小】）

cv.namedWindow("mywin",cv.WINDOW_NORMAL) 
# ret1=cap.set(cv.CAP_PROP_FRAME_HEIGHT,480) #设置打开视频流的宽高，一般宽比高大
# ret2=cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
# if ret1==True and ret2==True:
#     print("setting for cap frame work")

while True:
    # 逐帧捕获
    ret, frame = cap.read() # 返回两个参数第一个为是否正确打开，正常TURE，错误FALSE ，第二个为img变量
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #图像颜色格式的转换器
    #保存文件
   #frame = cv.flip(frame, 0)  #功能是将是图片垂直翻转
    out.write(frame)
    # 显示结果帧e   
    cv.imshow('mywin', frame)
    key=cv.waitKey(1) 
    if key== ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release() #每次使用完之后都要释放摄像头和注销窗口
out.release()
cv.destroyAllWindows()