import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#roi是我们需要找到的对象或对象区域
roi = cv.imread('rose_red.png')
hsv = cv.cvtColor(roi,cv.COLOR_BGR2HSV)
#目标是我们搜索的图像
target = cv.imread('rose.png')
hsvt = cv.cvtColor(target,cv.COLOR_BGR2HSV)
# 使用calcHist查找直方图。也可以使用np.histogram2d完成
M = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )

#通过直方图检测，查找同类元素
