import numpy as np
import cv2 as cv
img1=cv.imread("./sources/1.jpg") #背景
img2=cv.imread("./sources/cv.png") #前景

#切片
# img1=img1[0:800,0:1000]
# img2=img2[0:800,0:1000]
print(img1.shape,'\n',img2.shape)

cv.namedWindow("mywin1",cv.WINDOW_NORMAL)
cv.namedWindow("mywin2",cv.WINDOW_NORMAL)
cv.namedWindow("mywin3",cv.WINDOW_NORMAL)

# dst = cv.addWeighted(img1,0.7,img2,0.3,0) #两个图像相融合，需要尺寸和颜色通道相符和



rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
img2_1=img2[0:rows, 0:cols ]
# 现在创建logo的掩码，并同时创建其相反掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY) #转换成黑白，相当于二值化
print(img2gray)
cv.imshow("mywin1",img2gray)  
print(img1.dtype)
print(img2.dtype)
print(img2gray.dtype) 

ret, mask = cv.threshold(img2, 10, 255, cv.THRESH_BINARY)
mask =cv.cvtColor(mask,cv.COLOR_BGR2GRAY) 


ret, mask = cv.threshold(mask, 10, 255, cv.THRESH_BINARY)
cv.imshow("mywin2",mask)  
#阈值处理来创建logo的掩码。在这里，我们将灰度图像中的像素值小于10的像素设置为255（白色），其余像素设置为0（黑色）
mask_inv = cv.bitwise_not(mask)
cv.imshow("mywin3",mask_inv)  


# 现在将ROI中logo的区域涂黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# 仅从logo图像中提取logo区域
img2_fg = cv.bitwise_and(img2_1,img2_1,mask = mask)
# 将logo放入ROI并修改主图像
dst = cv.add(img1_bg,img2_fg)

# cv.imshow("mywin1",img1_bg)
# cv.imshow("mywin2",img2_fg)
# cv.imshow("mywin3",mask) 

img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)

cv.waitKey(0)
cv.destroyAllWindows()