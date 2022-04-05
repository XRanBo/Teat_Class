import cv2 as cv
 
camera_number = 0
cameraCapture = cv.VideoCapture(camera_number + cv.CAP_DSHOW)
fps = 30
size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
out = cv.VideoWriter("E:\\Test.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'),
                     fps, size)
 
success, frame = cameraCapture.read()
numFrameRemaining = 5 * fps - 1  
while success and cv.waitKey(1) and numFrameRemaining > 0:
    out.write(frame)
    success, frame = cameraCapture.read()
    cv.imshow("camera", frame)
    numFrameRemaining -= 1
    if numFrameRemaining == 0:
        print("success")
 
cameraCapture.release()
out.release()
cv.destroyAllWindows()
