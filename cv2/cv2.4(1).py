import numpy as np
import cv2 as cv
import math
drawing = False # 如果按下鼠标，则为真
mode = True # 如果为真，绘制矩形。按 m 键可以切换到曲线
ix,iy = -1,-1
# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        print("down")
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        print("move ")
        # if drawing == True:
        #     if mode == True:
        #         cv.rectangle(img,(ix,iy),(x,y),(0,255,0),6)
        #     else:
        #         cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP: #鼠标左键释放
        print("up ")
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),6) #画方框
        else:
            cv.circle(img,(ix,iy),int(math.sqrt((x-ix)**2 +(y-iy)**2)),(0,0,255),3)  #画圆

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle) #鼠标事件，每次都会产生中断，然后调用回调函数
while(1):
    cv.imshow('image',img)
    key=cv.waitKey(20)
    if  key & 0xFF == 27:
        break
    elif key== ord('m'):
        mode=~mode 
        print("mode switch ")
cv.destroyAllWindows()