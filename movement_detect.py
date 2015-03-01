""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
kernel = np.ones((21,21),'uint8')
boundaries = [([20,20,20],[170,150,150])]

while(True):
    ret, frame = cap.read()
    #faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    '''
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        cv2.circle(frame,(x + w/4, y + h/3), (w+h)/30, (0,0,255),-1)
        cv2.circle(frame,(x + 3*w/4, y + h/3), (w+h)/20, (0,0,255),-1)
        cv2.ellipse(frame,(x + w/2, y + 4*h/5),(w/5,h/10),0,0,180,255,-1)
    '''
    #try: diff = frame - frame_old
    try: diff = cv2.absdiff(frame,frame_old)
    except: 
        frame_old = frame
        continue
    '''
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper,dtype="uint8")

        mask = cv2.inRange(diff, lower, upper)
        output = cv2.bitwise_and(diff, diff, mask = mask)
    '''
        
    # Display the resulting frame
    cv2.imshow('frame',diff)

    frame_old = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
