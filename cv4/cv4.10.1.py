import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sources/1.jpg')
print(img.shape)
# cv.imshow("win",img)

# plt.hist(img.ravel(),16,[0,256]); plt.show()  #使用plt自带的直方图绘制函数，不需要cv.calHist

##bgr 三种颜色分别分析  在imread（）的时候记得打开多通道
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()


# create a mask
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:600, 100:600] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
# 计算掩码区域和非掩码区域的直方图
# 检查作为掩码的第三个参数
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
