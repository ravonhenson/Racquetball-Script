# steps:
# record 
# launch ball
# measure distance
# record data 
# export data to excel
# plot 

#things i probably need
# open cv 
# numpy 
# csv 
# excel something something something

import numpy as np 
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()