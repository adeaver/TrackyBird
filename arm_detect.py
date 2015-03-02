""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)

print "Step out of frame"
time.sleep(4)
print "Taking back"
for i in xrange(100):
    ret, BACK = cap.read()

BACK = cv2.cvtColor(BACK,cv2.COLOR_BGR2GRAY)
print "Step back into frame"

i = 0
while(True):
    ret, frame = cap.read() 
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #frame = np.float32(frame)

    # Display the resulting frame
    '''
    output1 = cv2.pyrDown(frame)
    for x in xrange(4):
        output1 = cv2.pyrDown(output1)

    output1 = cv2.resize(output1, (640,480))
    output2 = cv2.flip(frame,1)
    '''

    #cv2.imshow('frame',np.vstack( [np.hstack([frame,output1]), np.hstack([output2,output3])]))
    #cv2.moveWindow('frame',0,0)
    diff = cv2.absdiff(frame,BACK)
    NPDIFF = frame - BACK
    cv2.imshow('frame',np.vstack( [np.hstack([BACK,diff]), np.hstack([frame,NPDIFF])] ))
    if i == 0:
        i = 1
        cv2.moveWindow('frame', 0,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
