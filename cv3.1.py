import numpy as np
import cv2 as cv
img=cv.imread("./sources/1.jpg")
print(img.shape)
print(img[100,100]) #一张图片在opencv里可以看做颜色数组的三维数组，第一维是颜色通道，第二维度是行，第三维度是列
print(img.item(100,100,0))
print(img.size)
print(img.dtype)
cv.namedWindow("mywin1",cv.WINDOW_NORMAL)
cv.namedWindow("mywin2",cv.WINDOW_NORMAL)
# ball=img[1180:1380,8:118]
ball = img[8:118, 1080:1180]  #非常坑的一个点，是从y范围 在x范围，按照数组的理解来，先确定行在确定列
img[100 :210,100:200]=ball
b,g,r = cv.split(img)
img1 = cv.merge((b,g,r))
while(1):
    cv.imshow("mywin1",img)
    cv.imshow("mywin2",img1)
    key=cv.waitKey(1)
    if key& 0xFF ==27 :
        break 
cv.destroyAllWindows()