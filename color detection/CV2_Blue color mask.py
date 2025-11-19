import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BAYER_BGR2HSV)
    
    #Blue color
    low_blue = np.array([161,155,84])
    high_blue = np.array([179,255,255])
    
    blue_mask = cv2.inRange(hsv_frame,low_blue,high_blue)
    blue = cv2.bitwise_and(frame,frame, mask=blue_mask)
    
    cv2.imshow("Frame",frame)
    
    cv2.imshow("Blue",blue)
    
    key = cv2.waitkey(1)
    if key == 27:
        break