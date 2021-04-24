import cv2


filename = "data-1-2.csv"


map_name = "photo_2021-04-24_10-17-12.jpg"
img = cv2.imread(map_name)
imgWidth = 1280
imgHeight = 400
video_speed = 2



fourcc = cv2.VideoWriter_fourcc(*'DIVX')
videoWriter = cv2.VideoWriter("output.avi", fourcc, video_speed , (imgWidth, imgHeight))

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