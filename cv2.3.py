import numpy as np
import cv2 as cv
# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8) #创建图像
# 绘制一条厚度为5的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),5)  #画线（【img变量】【起点】【终点】【颜色】【线厚度】）
cv.rectangle(img,(384,0),(510,128),(0,255,0),3) #画矩形 两个点（左上角和右下角）就可以确定
cv.circle(img,(447,63), 63, (0,0,255), -1) #画圆，圆心和半径 后面的-1是线厚度，-1表示填充满封闭图形
cv.ellipse(img,(256,256),(100,50),0,0,360,(0,50,100),-1)#椭圆 自心点 长短轴 角度 。。
#画多边形 多点围成
pts = np.array([[10,5],[20,30],[70,20]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255)) #画点，中间的true标识连成封闭图形
#文字标识
font = cv.FONT_HERSHEY_SIMPLEX #选择字体
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)  # 标注文字，开始的左下角坐标

cv.imshow("mywin",img)
key=cv.waitKey(0)
if key!=None:
    pass
cv.destroyAllWindows()