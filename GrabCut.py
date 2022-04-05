import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.pyrDown(cv2.imread("D://data.jpg", cv2.IMREAD_UNCHANGED))
#二值化,cv2.threshold()函数功能是像素高于阈值时，给像素赋予新值。这儿参数是对于像素值高于127的，赋值255.
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY),
                            127, 255, cv2.THRESH_BINARY)
#轮廓提取,findContour用于找到不规则形状的轮廓
contours, hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    #计算一个简单的边界框，通过顶点绘制的矩形
    # 将轮廓信息转化为(x,y)坐标，并返回宽和高
    x,y,w,h = cv2.boundingRect(contour)
    
    #画出边界框
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255),2)
    # rectangle有四个参数：要绘制的图像，左上角坐标，右下角坐标，颜色，轮廓宽度（这里为2）
   
    #计算包围目标的最小矩形区域，中心点坐标、宽度高度，旋转角度
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)# 获得矩形四个角的坐标, 返回浮点型
    box = np.int0(box)# 把浮点型转化为整型，访问坐标必须是整数
    cv2.drawContours(img, [box], 0, (255,0,255), 2)

 
img = cv2.drawContours(img, contours, -1, (255,0,0), 1)#使用cv2.drawContours()函数绘制最小矩形区域。
cv2.imshow("findcontour",img)

# 创建一个和加载图像一样形状的 填充为0的掩膜
mask = np.zeros(img.shape[:2], np.uint8)

# 创建以0填充的前景和背景模型
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 定义一个矩形
rect = (x, y, w, h)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img*mask2[:, :, np.newaxis]

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread("D://data.jpg"), cv2.COLOR_BGR2RGB))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()