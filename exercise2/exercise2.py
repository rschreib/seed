#Robert Schreibman
#EENG450 SEED LAB
#Exercise 2: Intro to Open CV

#An introduction to using the pi camera and OpenCV

from picamera import PiCamera
import picamera
import picamera.array
from time import sleep
import os
import numpy as np
import cv2


camera = PiCamera()

camera.rotation = 180
camera.resolution = (1024, 768) 
folderpath = "/home/pi/Desktop"         
filename = "1.jpg"                      #default value
mouseX = 0
mouseY = 0

'''
with picamera.array.PiRGBArray(camera) as output:
        camera.capture(output, 'rgb')
        print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))
        print(output)
        img = cv2.imread(output)
        cv2.imshow(output, img)
        '''
def captureImage():
        print("Look into Camera ...")
        #camera.start_preview()
        for x in range(3, 0, -1):
                sleep(1)
                print(x)
        camera.capture('%s/.image.jpg' % folderpath)
        #camera.stop_preview()

def storeFile(name):
        os.system('mv %s/.image.jpg %s/%s' % (folderpath, folderpath, name))
        print("Succesfully created %s on Desktop" % name)

def draw_circle(event,x,y,flags, param):
        global mouseX,mouseY
        if event == cv2.EVENT_LBUTTONDBLCLK:
                #cv2.circle(img,(x,y),100,(255,0,0),-1)
                mouseX,mouseY = x,y
                print("x:",mouseX,"y:",mouseY)
                '''
                with picamera.PiCamera() as camera:
                        with picamera.array.PiRGBArray(camera) as output:
                                camera.capture(output, 'rbg')
                                print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))'''
                                
        
def function1():
        # 1a  ##################################################################
        captureImage()

        # 1b  ##################################################################
        #filename = input("Image Filename (.jpg): ")
        #filename = filename + ".jpg"
        filename = "1.jpg"
        # 1c  ##################################################################
        storeFile(filename)

        # 1d  ##################################################################
        print("\nNow select a Pixel on the Image...\n")
        global img
        img = cv2.imread('%s/%s' % (folderpath, filename))
  
        # 1e  ##################################################################
        cv2.namedWindow('Image Captured',1)
        cv2.setMouseCallback('Image Captured', draw_circle)
        cv2.imshow('Image Captured', img)                                        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

function1()

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
        os.system('cp %s/colors.jpg %s/colors-copy.jpg' % (folderpath, folderpath))

        # 3d  ##################################################################
        img = cv2.imread('/home/pi/Desktop/colors.jpg',1)
        small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        cv2.imshow('Image', small)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('/home/pi/Desktop/colors.jpg',small)
        
        # 3e  ##################################################################

        
        
        # 3f  ##################################################################
        img1 = cv2.imread('/home/pi/Desktop/colors.jpg',1)
        img2 = cv2.imread('/home/pi/Desktop/colors-copy.jpg',1)
        cv2.imshow('Original Image', img1)
        cv2.imshow('Copy Image', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
# 4   ##################################################################

# 5   ##################################################################

# 6   ##################################################################

# 7a  ##################################################################
# 7b  ##################################################################
# 7c  ##################################################################
