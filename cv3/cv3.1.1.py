#用matplotlib 制作边框，不过感觉没啥效果
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img = cv.imread("./sources/p1.png") 
img1=cv.cvtColor(img,cv.COLOR_BGR2RGB)
replicate = cv.copyMakeBorder(img1,50,50,50,50,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,50,50,50,50,cv.BORDER_REFLECT)
reflect501 = cv.copyMakeBorder(img1,50,50,50,50,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,50,50,50,50,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,50,50,50,50,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect501,'gray'),plt.title('REFLECT_501')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
