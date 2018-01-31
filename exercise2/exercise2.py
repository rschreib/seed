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
filename = "1.jpg"
dst = "/home/pi/Desktop/11.jpg"

def captureImage():
        print("Look into Camera ...")
        #camera.start_preview()
        for x in range(3, 0, -1):
                sleep(1)
                print(x)
        camera.capture('%s/.image.jpg' %folderpath)
        #camera.stop_preview()

def storeFile(name):
        os.system('mv %s/.image.jpg %s/%s' % (folderpath, folderpath, name))
        print("Succesfully created %s on Desktop" % name) 

def function1():
        # 1a  ##################################################################
        captureImage()

        # 1b  ##################################################################
        filename = input("Image Filename (.jpg): ")
        filename = filename + ".jpg"

        # 1c  ##################################################################
        storeFile(filename)

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
        #stuck here, need to click on image and get location


def function2():
        # 2   ##################################################################
        img = cv2.imread('/home/pi/Desktop/1.jpg',1)
        small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        print("original dim: ", img.shape)
        print("new dim: ", small.shape)
        cv2.imshow('Image', small)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def function3():
        # 3a  ##################################################################
        captureImage()

        # 3b  ##################################################################
        storeFile("colors.jpg")
        
        # 3c  ##################################################################
        img = cv2.imread('/home/pi/Desktop/colors.jpg',1)
        small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        cv2.imshow('Image', small)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # 3d  ##################################################################
        # 3e  ##################################################################
        # 3f  ##################################################################
function3()

# 4   ##################################################################

# 5   ##################################################################

# 6   ##################################################################

# 7a  ##################################################################
# 7b  ##################################################################
# 7c  ##################################################################
