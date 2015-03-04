from movement_detect import *
import cv2

video = Movement_Track()
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
print video.maxy, video.miny

while True:
    print video.Movement()
    ret,frame = video.cap.read()
    frame = cv2.pyrDown(frame)
    cv2.line(frame, (0, int(video.avg)), (frame.shape[1], int(video.avg)), (0,0,255), 5)
    cv2.line(frame, (0, int(video.maxy)), (frame.shape[1], int(video.maxy)), (0,255,0), 5)
    cv2.line(frame, (0, int(video.miny)), (frame.shape[1], int(video.miny)), (255,0,0), 5)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

