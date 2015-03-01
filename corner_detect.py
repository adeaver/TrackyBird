""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, real = cap.read() 
    frame = cv2.cvtColor(real,cv2.COLOR_BGR2GRAY)
    frame = np.float32(frame)

    dst = cv2.cornerHarris(frame,2,3,0.01)
    dst = cv2.dilate(dst, None)
    real[dst>0.01*dst.max()] = [0,0,255]

    cv2.imshow('frame',real)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
