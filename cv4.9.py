import numpy as np
import cv2 as cv
im = cv.imread('./sources/cv.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #找出边缘的轮廓链点，返回给contours
cv.drawContours(imgray, contours, -1, (255,0,0), 5)
cv.imshow("wim1",imgray)

cv.waitKey(0)
cv.destroyAllWindows()
