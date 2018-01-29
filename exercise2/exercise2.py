#Robert Schreibman
#EENG450 SEED LAB
#Exercise 2: Intro to Open CV

#An introduction to using the pi camera and OpenCV

from picamera import PiCamera
from time import sleep
import os
from PIL import Image

import sys
import subprocess
def openImage(path):
	imageViewer = {'linux':'eog','win32':'explorer','darwin':'open'}[sys.platform]
	subprocess.run([imageViewer, /home/pi/Desktop/%s

camera = PiCamera()
camera.rotation = 180


# 1a
print("Look into Camera ...")
#camera.start_preview()
for x in range(3, 0, -1):
	sleep(1)
	print(x)
camera.capture('/home/pi/Desktop/.image.jpg')
#camera.stop_preview()

# 1b
filename = input("Image Filename (.jpg): ")

# 1c
os.system('mv /home/pi/Desktop/.image.jpg /home/pi/Desktop/%s' % filename)
print("Succesfully created %s on Desktop" % filename) 
#os.system('echo "Succesfully created %s on Desktop"' % filename) 

# 1d
img = Image.open('/home/pi/Desktop/%s' % filename)



