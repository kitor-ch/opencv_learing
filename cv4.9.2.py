import numpy as np
import cv2 as cv

img = cv.imread('./sources/j.png',0)
ret,thresh = cv.threshold(img,25,255,0) 
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)

epsilon = 0.1*cv.arcLength(cnt,False) 
approx = cv.approxPolyDP(cnt,epsilon,False)
cv.drawContours(img, approx, -1, (255,0,0), 5)

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("wim1",img)
print( M )
print(cv.arcLength(cnt,True))

cv.waitKey(0)
cv.destroyAllWindows()