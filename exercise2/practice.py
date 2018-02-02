#Practice Functions

from picamera import PiCamera
import picamera
import picamera.array
from time import sleep
import os
import numpy as np
import cv2


img1 = cv2.imread('/home/pi/Desktop/colors.jpg',1)
print(img1[(1,1)][2])
print(img1.shape[0])
