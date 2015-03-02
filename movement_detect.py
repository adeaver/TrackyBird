""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

boundaries = [ ([50,30,30], [145,133,128]) ]

while(True):
    ret, frame = cap.read()

    try: 
        diff = cv2.absdiff(frame,frame_old)
        diff_np = frame - frame_old
        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            mask = cv2.inRange(diff_np, lower, upper)
            diff_np = cv2.bitwise_and(frame,frame, mask=mask)
    except: 
        frame_old = frame
        continue
        
    # Display the resulting frame
    cv2.imshow('frame',np.hstack([diff,diff_np]))

    frame_old = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
