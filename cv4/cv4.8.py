#图像金字塔  可以用于两张图的平滑连接
import cv2 as cv
import numpy as np,sys
A = cv.imread('./sources/apple.jpg')
B = cv.imread('./sources/orange.jpg')
# 生成A的高斯金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
# 生成B的高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)
# 生成A的拉普拉斯金字塔
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)
# 生成B的拉普拉斯金字塔
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)
# 现在在每个级别中添加左右两半图像 
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:])) #la和lb里面的参数需要是整数，所以要取整
    LS.append(ls)
# 现在重建
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
# 图像与直接连接的每一半
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
# cv.imwrite('./sources/Pyramid_blending2.jpg',ls_)
# cv.imwrite('./sources/Direct_blending.jpg',real)
cv.imshow("wim1",ls_)
cv.imshow("wim2",real)

cv.waitKey(0)
cv.destroyAllWindows()
