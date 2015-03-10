import cv2
import numpy as np

class Movement_Track:
    def __init__(self,video=0):
        self.cap = cv2.VideoCapture(video)

        # Values for cleaning up motion tracking
        self.boundaries = [ ([50,30,30], [145,133,128]) ]
   
        #self.starter = 0 
        #self.frame_old = []
        self.color = (0,0,0)
        self.prev = 0 # previous y position

        ret, self.frame_old = self.cap.read()
        frame = cv2.pyrDown(self.frame_old)
        self.height = frame.shape[0]
        self.width = frame.shape[1]
        self.thresh = 50

        # Initializing these at respective values
        # to allow for centering around motion centers
        # of the user
        self.maxy = 0 # maximum y value reached
        self.miny = self.height # minimum y value reached
        self.avg = self.height/2.0 # Initial average value

        self.maxx = 0
        self.minx = 0

    def Get_Color(self):
        ret, frame = self.cap.read()
        self.color = cv2.mean(frame)[:3]
        return self.color

    def Movement(self):
        y = self.Get_Move()
        if y == 0:
            return False

        if y > self.maxy:
            self.maxy = y
            self.avg = (self.maxy + self.miny)/2.0

        if y < self.miny:
            self.miny = y
            self.avg = (self.maxy + self.miny)/2.0

        if y > self.avg and self.prev < self.avg:
            if (self.maxx - self.minx) > 50 \
                    and self.maxx-self.thresh > self.width/2 \
                    and self.minx+self.thresh < self.width/2:
                self.prev = y
                return True
            return False
        else:
            self.prev = y
            return False

    def Get_Move(self):
        ret, frame = self.cap.read()

        diff_np = frame - self.frame_old

        for (lower, upper) in self.boundaries:
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            mask = cv2.inRange(diff_np, lower, upper)
            
        mask = cv2.pyrDown(mask)
        white_x = []
        white_y = []
        for y in xrange( mask.shape[0] ):
            for x in xrange( mask.shape[1] ):
                if mask.item(y,x) == 255:
                    white_x.append(x)
                    white_y.append(y)
        if len(white_x) > 0:
            self.minx = min(white_x)
            self.maxx = max(white_x)

        avg_y = sum(white_y) / float(len(white_y)+0.1)
        
        self.frame_old = frame
    
        return avg_y

    def destroy(self):
        cap.release()
        cv2.destroyAllWindows()
