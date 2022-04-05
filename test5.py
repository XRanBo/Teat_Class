import cv2
import numpy as np
#函数 cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
img = cv2.pyrDown(cv2.imread("D://test2.jpg", cv2.IMREAD_UNCHANGED))
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

    # 绘制最小闭圆
    #cv2.minEnclosingCircle函数返回一个二元组，第一个元组为圆心坐标，第二个为半径
    (x0,y0), radius = cv2.minEnclosingCircle(contour)
    center = (int(x0), int(y0))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0,255,255),2)
 
cv2.drawContours(img, contours, -1, (255,0,0), 1)#使用cv2.drawContours()函数绘制最小矩形区域。
cv2.imshow("findcontour",img)
cv2.waitKey()
cv2.destroyAllWindows()
# 使用cv2.threshold()函数进行二值化处理。
# 使用cv2.findContours()函数检测轮廓。
# 使用cv2.boundingRect()函数获得边界框。
# 使用cv2.rectangle()函数绘制边界框。
# 使用cv2.minAreaRect()函数获得最小矩形区域。
# 使用cv2.drawContours()函数绘制最小矩形区域。
# 使用cv2.minEnclosingCircle()函数获得最小闭圆。
# 使用cv2.circle()函数绘制最小闭圆。