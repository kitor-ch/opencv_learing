import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img1 = cv.imread('./sources/cv.png')
img=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
# img1=cv.cvtColor(img1,cv.COLOR_BGR2RGB)
#静态阈值
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img1, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

#动态阈值
thresh6 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
#动态阈值，只能处理灰度图片
cv.imshow("win1",img)
cv.imshow("win",thresh6)
cv.waitKey(0)
cv.destroyAllWindows()

