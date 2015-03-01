""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
        
    # Display the resulting frame
    '''
    output = cv2.pyrDown(frame)
    for x in xrange(5):
        output = cv2.pyrDown(output)
    '''
    output = cv2.Laplacian(frame, 6)
    
    output = cv2.resize(output, (640,480))
    cv2.imshow('frame',np.hstack([frame,output]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
