""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    try: diff = cv2.absdiff(frame,frame_old)
    except: 
        frame_old = frame
        continue
        
    # Display the resulting frame
    cv2.imshow('frame',diff)

    frame_old = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
