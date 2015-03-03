""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

boundaries = [ ([50,30,30], [145,133,128]) ]

starter = 0
while(True):
#for x in xrange(3):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.blur(frame, (5,5) )

    if starter == 0:
        frame_old = frame
        starter = 1
        continue

    diff_np = frame - frame_old

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(diff_np, lower, upper)
        diff_np = cv2.bitwise_and(frame,frame, mask=mask)
        
    mask = cv2.pyrDown(mask)
    # Display the resulting frame
    #cv2.imshow('frame',np.hstack([diff,diff_np]))
    white_x = []
    white_y = []
    for y in xrange( mask.shape[0] ):
        for x in xrange( mask.shape[1] ):
            if mask.item(y,x) == 255:
                white_x.append(x)
                white_y.append(y)

    cv2.imshow('mask',mask)
    avg_y = sum(white_y) / float(len(white_y)+0.1)
    print avg_y
    
    #cv2.imshow('orig', cv2.sort(frame, CV_SORT_DESCENDING) )
    #print cv2.mean( cv2.pow(mask,2) )

    frame_old = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
