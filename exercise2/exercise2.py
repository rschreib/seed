#Robert Schreibman
#EENG450 SEED LAB
#Exercise 2: Intro to Open CV

#An introduction to using the pi camera and OpenCV

from picamera import PiCamera
from time import sleep
import os
import numpy as np
import cv2

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1024, 768) 
folderpath = "/home/pi/Desktop"


# 1a  ##################################################################
print("Look into Camera ...")
#camera.start_preview()
for x in range(3, 0, -1):
	sleep(1)
	print(x)
camera.capture('%s/.image.jpg' %folderpath)
#camera.stop_preview()

# 1b  ##################################################################
filename = input("Image Filename (.jpg): ")
filename = filename + ".jpg"

# 1c  ##################################################################
os.system('mv %s/.image.jpg %s/%s' % (folderpath, folderpath, filename))
print("Succesfully created %s on Desktop" % filename) 
#os.system('echo "Succesfully created %s on Desktop"' % filename) 

# 1d  ##################################################################
img = cv2.imread('%s/%s' % (folderpath, filename))
cv2.imshow('Image Captured', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1e  ##################################################################
sleep(2)
print("\nNow select a Pixel on the Image...\n")
sleep(2)
myfile = open('%s/%s' % (folderpath, filename))


# 2   ##################################################################
# 3a  ##################################################################
# 3b  ##################################################################
# 3c  ##################################################################
# 3d  ##################################################################
# 3e  ##################################################################
# 3f  ##################################################################

# 4   ##################################################################

# 5   ##################################################################

# 6   ##################################################################

# 7a  ##################################################################
# 7b  ##################################################################
# 7c  ##################################################################
