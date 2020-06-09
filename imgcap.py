import cv2
import time

import threading

cam = cv2.VideoCapture(0)

cv2.namedWindow("Smart Parking")

img_counter = 0
prevCapTime = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Smart Parking", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    # elif k%256 == 32: capturing image by space
        # SPACE pressed
    img_name = "CarVidCap_{}.png".format(img_counter)
    now = time.time()
    sub = now - prevCapTime
    if  sub >= 5:
        img_counter += 1
        cv2.imwrite(img_name, frame)
        prevCapTime = time.time()
        print(img_name + "-capped"," has been captured !!!!")
        print("Cap time is :      ", sub)
    

cam.release()

cv2.destroyAllWindows()