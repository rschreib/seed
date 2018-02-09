import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob

camera = PiCamera()
rawCapture = PiRGBArray(camera)

#camera.iso = 100

#Auto White Baance Section
#time.sleep(2)
#g = ((341/256),(217/128))
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g

camera.iso = 400
camera.shutter_speed = 3000

camera.capture(rawCapture, format="bgr")
img = rawCapture.array
cv2.imwrite('test2.jpg',img)

img = cv2.resize(img,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0,230,130])
upper = np.array([180,255,255])

mask = cv2.inRange(hsv,lower,upper)

kernal = np.ones((5,5),np.uint8)
mask = cv2.erode(mask,kernal,iterations = 1)
#mask = cv2.dilate(mask,kernal,iterations = 1)

res = cv2.bitwise_and(img,img,mask=mask)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 1;
params.maxThreshold = 200;

params.filterByArea = True
params.minArea = 5

detector = cv2.SimpleBlobDetector(params)

keypoints = detector.detect(mask)
print(len(keypoints))

cv2.imshow('res',mask)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
