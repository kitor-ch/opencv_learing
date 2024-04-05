import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('sources/1.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256]) #用cv的算法
h,s=hsv[:,:,0],hsv[:,:,1]
hist1, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]]) #用numpy的算法

cv.imshow("w1",img)
cv.imshow("w2",hsv)
cv.imshow("w3",hist)
cv.imshow("w4",hist1)

plt.imshow(hist1,interpolation = 'nearest')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

#X轴显示S值，Y轴显示色相。