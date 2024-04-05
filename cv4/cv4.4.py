#图像平滑 让图像变得模糊或者叫滤波
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sources/cv.png') 
kernel = np.ones((5,5),np.float32)/25  #生成矩阵 5x5的矩阵，np。float类型
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(5,5)) #效果和filter2D的差不多
Gaussianblur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])   #将x和y轴的刻度标签设置为空列表，从而隐藏了x轴上的刻度。
plt.subplot(222),plt.imshow(dst),plt.title('Averaging')
plt.subplot(223),plt.imshow(blur),plt.title('Blur')
plt.subplot(224),plt.imshow(Gaussianblur),plt.title('GaussianBlur')
plt.show()