import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('E:\\XBW.mp4',fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print('false')
        break
    
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame = cv.flip(gray, 1)
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows() 
