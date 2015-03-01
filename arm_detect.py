""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() 
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = np.float32(frame)

    # Display the resulting frame
    '''
    output1 = cv2.pyrDown(frame)
    for x in xrange(4):
        output1 = cv2.pyrDown(output1)

    output1 = cv2.resize(output1, (640,480))
    output2 = cv2.flip(frame,1)
    '''

    output3 = frame
    dst = cv2.cornerHarris(frame,2,3,0.04)
    dst = cv2.dilate(dst, None)
    output3[dst>0.01*dst.max()] = [0,0,255]

    #cv2.imshow('frame',np.vstack( [np.hstack([frame,output1]), np.hstack([output2,output3])]))
    #cv2.moveWindow('frame',0,0)
    cv2.imshow('frame',output3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
