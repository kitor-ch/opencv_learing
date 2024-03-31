import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sources/num.png') #图像可以是彩色也可以是灰度
laplacian = cv.Laplacian(img,cv.CV_64F)  #拉普拉斯梯度算法 原理是矩阵相乘
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5) #x方向的梯度倒数
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)  #y方向的梯度倒数
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()