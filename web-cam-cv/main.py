import cv2
import numpy as np

vid = cv2.VideoCapture(0)
while 1:
    ret, frame = vid.read()
    if ret:
        ### NOTE: Size, Crop and Rotation
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame = cv2.resize(frame,(400,700),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        frame = frame[:400, :600]
        ###
        ### NOTE: Contrast and Brightness
        cv2.normalize(frame, frame, 0, 182, cv2.NORM_MINMAX)
        ###
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vid.release()