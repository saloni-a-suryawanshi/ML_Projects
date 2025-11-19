import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BAYER_BGR2HSV)
    
    
    cv2.imshow("frame",frame)
    
    key = cv2.waitkey(1)
    if key == 27:
        break
    

