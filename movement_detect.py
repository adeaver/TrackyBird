import cv2
import numpy as np
cap = cv2.VideoCapture(0)

boundaries = [ ([50,30,30], [145,133,128]) ]

starter = 0
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #frame = cv2.blur(frame, (5,5) )

    if starter == 0:
        frame_old = frame
        starter = 1
        continue

    diff_np = frame - frame_old

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(diff_np, lower, upper)
        
    mask = cv2.pyrDown(mask)
    frame2 = cv2.pyrDown(frame)
    white_x = []
    white_y = []
    for y in xrange( mask.shape[0] ):
        for x in xrange( mask.shape[1] ):
            if mask.item(y,x) == 255:
                white_x.append(x)
                white_y.append(y)

    avg_y = sum(white_y) / float(len(white_y)+0.1)
    avg_x = sum(white_x) / float(len(white_x)+0.1)

    color = cv2.mean(frame)[:3]
    #color = cv2.max(frame,frame)[:3]
    #color = cv2.mean(color)[:3]
    #color = (10,100,10)
    if avg_x != 0 and avg_y != 0:  
        cv2.circle(frame2, (int(avg_x), int(avg_y)), 10, color, -1) 

    cv2.imshow('frame', frame2)
    cv2.imshow('mask', mask)

    
    frame_old = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
