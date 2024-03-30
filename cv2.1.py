import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#加载彩色灰度图像
img = cv.imread('./sources/1.jpg',-1) # 相当与打开一个文件。（【文件地址】，【颜色参数，0是灰色，1是彩色,还有个-1不知道】）
cv.namedWindow('image',cv.WINDOW_NORMAL) # 创建窗口，（【窗口名称】，【窗口属性】）
cv.imshow('image',img)     #创建一个窗口显示图像，（【窗口名称】，【img变量】）

#使用matplot显示
img_plt=cv.cvtColor(img, cv.COLOR_BGR2RGB) #将cv的图像格式换成matplot的格式 （cv是BGR格式，plt是RGB格式）
plt.imshow(img_plt, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()

k=cv.waitKey(0)  #等待按键事件，0是任何按键，也可以设置为特定的按键
print(k)
if k==ord('s'):  #将字符的转为uincode 的编码
    cv.imwrite('./sources/img_out.png',img) #保存图像（【文件名（可指定路径】，【img变量】）
    cv.destroyAllWindows() #毁灭所有的窗口
else :
    cv.destroyAllWindows()