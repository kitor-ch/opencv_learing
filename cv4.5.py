import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./sources/j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1) #侵蚀
dilation = cv.dilate(img,kernel,iterations = 1)  #扩张 
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  #开运算，先侵蚀再扩张 适合消去外的噪点
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  #闭运算，先扩张再侵蚀 适合消去里的噪点
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)  #轮廓
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)   
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel) 

plt.subplot(241),plt.imshow(img),plt.title('img')
plt.subplot(242),plt.imshow(erosion),plt.title('erosion')
plt.subplot(243),plt.imshow(dilation),plt.title('dilation')
plt.subplot(244),plt.imshow(opening),plt.title('opening')
plt.subplot(245),plt.imshow(closing),plt.title('closing')
plt.subplot(246),plt.imshow(gradient),plt.title('gradient')
plt.subplot(247),plt.imshow(tophat),plt.title('tophat')
plt.subplot(248),plt.imshow(blackhat),plt.title('blackhat')
plt.show()