import numpy as np
import cv2
#使用普通摄像头进行深度估计
def update(val=0):
    #为“alone”图像对调整视差范围
    stereo.setBlockSize(cv2.getTrackbarPos('window_size','disparity'))# 从，5~21之间为宜
    #SAD窗口大小，容许范围是[5,255]，一般应该在 5x5..21x21 之间，参数必须为奇数值, int型。 
    stereo.setUniquenessRatio(cv2.getTrackbarPos('uniquenessRatio','disparity'))#uniquenessRatio主要可以防止误
    #UniquenessRatio主要可以防止误匹配，此参数对于最后的匹配结果是有很大的影响。
    # 立体匹配中，宁愿区域无法匹配，也不要误匹配。如果有误匹配的话，碰到障碍检测这种应用，就会很麻烦。
    # 该参数不能为负值，一般5-15左右的值比较合适，int型。 
    stereo.setSpeckleWindowSize(cv2.getTrackbarPos('speckleWindowSize','disparity'))
    stereo.setSpeckleRange(cv2.getTrackbarPos('speckleRange','disparity'))
    stereo.setDisp12MaxDiff(cv2.getTrackbarPos('disp12MaxDiff','disparity'))

    print('computing disparity')
    disp = stereo.compute(imgL,imgR).astype(np.float32)/16.0

    cv2.imshow('left',imgL)
    cv2.imshow('Right',imgR)
    cv2.imshow('disparity',(disp-min_disp)/num_disp)
   
 

if __name__ == "__main__":
    window_size =5
    min_disp =16
    num_disp =192-min_disp
    #视差窗口，即最大视差值与最小视差值之差,窗口大小必须是 16的整数倍，int型。
    blockSize = window_size
    uniquenessRatio = 1
    speckleRange = 3
    speckleWindowSize =3
    disp12MaxDiff =200
    P1 = 600
    P2 = 2400
    imgL = cv2.imread('D://test6.jpg') #加载图像
    imgR = cv2.imread('D://test7.jpg')
    cv2.namedWindow('disparity')
    

    cv2.createTrackbar('speckleRange','disparity',speckleRange,50,update)
    cv2.createTrackbar('window_size','disparity',window_size,21,update)
    cv2.createTrackbar('speckleWindowSize','disparity',speckleWindowSize,200,update)
    cv2.createTrackbar('uniquenessRatio','disparity',uniquenessRatio,50,update)
    cv2.createTrackbar('disp12MaxDiff','disparity',disp12MaxDiff,250,update)
    stereo =cv2.StereoSGBM_create(
        minDisparity = min_disp,
        numDisparities=num_disp,
        blockSize = window_size,
        uniquenessRatio = uniquenessRatio,
        speckleRange = speckleRange,
        speckleWindowSize = speckleWindowSize,
        disp12MaxDiff = disp12MaxDiff,
        P1 = P1,
        P2 = P2
    )
    update()
    cv2.waitKey()
