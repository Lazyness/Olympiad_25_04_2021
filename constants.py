import cv2


filename = "data-1-2.csv"


map_name = "photo_2021-04-24_10-17-12.jpg"
img = cv2.imread(map_name)
imgWidth = 1280
imgHeight = 400
video_speed = 10

videoname = "output.avi"
printfile = "raport.txt"

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
videoWriter = cv2.VideoWriter(videoname, fourcc, video_speed , (imgWidth, imgHeight))

cordB1 = [1091,271]
cordB2 = [1091,121]
cordB3 = [176,121]
cordB4 = [176,263]
cordB5 = [743,130]
cordB6 = [568,220]
cv2.imshow("sad",img)
cv2.waitKey(1)

r = [0,0,255]
n = None
divace_texture = [
    [n,n,r,r,r,r,r,n,n],
    [n,r,r,r,r,r,r,r,n],
    [r,r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r,r],
    [n,r,r,r,r,r,r,r,n],
    [n,n,r,r,r,r,r,n,n]
]

class Date():
    def __init__(self):
        self.b1 = -150
        self.b2 = -150
        self.b3 = -150
        self.b4 = -150
        self.b5 = -150
        self.b6 = -150
        self.c = 0
    
    def setb(self,b,val):
        self.c = self.c + 1
        val = int(val)
        if b == 1:
            self.b1 = val
        if b == 2:
            self.b2 = val
        if b == 3:
            self.b3 = val
        if b == 4:
            self.b4 = val
        if b == 5:
            self.b5= val
        if b == 6:
            self.b6 = val

    def get2max(self):
        
        if self.c < 10:
            return [-1000,-1000]
        arr = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6]
        m = max(arr)
        if m == self.b1:
            arr.pop(0)
            m = max(arr)
            if self.b2 == m:
                return [1000,200]
            else:
                return [900,200]
        if m == self.b2:
            arr.pop(1)
            m = max(arr)
            if self.b1 == m:
                return [1000,200]
            else:
                return [900,200]
        if m == self.b3:
            arr.pop(2)
            m = max(arr)
            if self.b4 == m:
                return [270,200]
            else:
                return [400,200]
        if m == self.b4:
            arr.pop(3)
            m = max(arr)
            if self.b3 == m:
                return [270,200]
            else:
                return [400,200]
        if m == self.b5:
            arr.pop(4)
            m = max(arr)
            if self.b6 == m:
                return [650,180]
            else:
                return [650,250]
        if m == self.b6:
            arr.pop(5)
            m = max(arr)
            if self.b5 == m:
                return [650,180]
            else:
                return [650,250]
        return [-1000,-1000]

datelast = Date()