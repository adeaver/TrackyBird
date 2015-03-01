""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200])]
'''
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]
'''

while(True):
    ret, frame = cap.read()

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
     
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask = mask)
    
        
    # Display the resulting frame
    cv2.imshow('frame',np.hstack([frame,output]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
