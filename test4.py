import cv2
import numpy as np 
from PIL import Image
import numpy as np
import random

# def sp_noise(image,prob):
#     output = np.zeros(image.shape,np.uint8)
#     thres = 1 - prob
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#     return output

img = cv2.imread("D:\\test.jpg",0)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # 添加椒盐噪声，噪声比例为 0.02
# out1 = sp_noise(img, prob=0.02)

# original_img = cv2.imread("D:\\test.jpg", 0)

# canny(): 边缘检测
# img1 = cv2.GaussianBlur(img,(3,3),0)
# canny = cv2.Canny(img1, 50, 150)
# canny2 = cv2.Canny(img1, 150, 300)
# # 椒盐后的边缘检测
# img2 = cv2.GaussianBlur(original_img,(3,3),0)
# canny2 = cv2.Canny(img, 50, 150)

# cv2.imshow('out1',out1)
# cv2.imshow("original_img", original_img) 
# cv2.imshow('img1', img1)
# cv2.imshow('Canny', canny)
# cv2.imshow('Canny2',canny2)




cv2.waitKey(0)
cv2.destroyAllWindows()




