from scipy import ndimage
import cv2
import numpy as np

kernel_3x3 = np.array([[-1,-1,-1],
                      [-1,8,-1],
                      [-1,-1,-1]])
kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                      [-1,1,2,1,-1],
                      [-1,2,1,2,-1],
                      [-1,2,-1,-2,-1],
                      [-1,-1,-1,-1,-1]])
img = cv2.imread('D:/test.jpg',0)

k3 = ndimage.convolve(img,kernel_3x3)
k5=ndimage.convolve(img,kernel_5x5)

blurred=cv2.GaussianBlur(img,(25,25),0)
g_hpf=img - blurred

cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("blurred",blurred)
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()