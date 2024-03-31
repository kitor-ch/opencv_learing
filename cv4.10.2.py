#通过像素直方图的均衡，增强视觉上的对比度，显得更加清晰

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sources/snow.jpg',0)
cv.imshow("win1",img)

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img] 
cv.imshow("win2",img2)

# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
