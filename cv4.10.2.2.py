#对比度受限的直方图均衡（小范围的均衡）可以解决只有局部的对比度太低的问题
import numpy as np
import cv2 as cv
img = cv.imread('./sources/clahe.jpg',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv.imshow("win1",img)
cv.imshow("win2",cl1)

cv.waitKey(0)
cv.destroyAllWindows()