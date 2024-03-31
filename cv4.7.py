#canny 边沿检测
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sources/cv.png') #彩色图比黑白具有更好的效果
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
edges = cv.Canny(img,100,200)
edges_gray=cv.Canny(img_gray,100,200)
plt.subplot(221),plt.imshow(img,cmap="gray")
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_gray)
plt.title('Original gray'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges_gray)
plt.title('Edge_gray'), plt.xticks([]), plt.yticks([])
plt.show()