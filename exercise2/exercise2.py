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

def get_pixel_location(event,x,y,flags, param):
        global mouseX,mouseY
        if event == cv2.EVENT_LBUTTONDBLCLK:
                mouseX,mouseY = x,y
                print("x:",mouseX,"y:",mouseY)
                print(img[(mouseY,mouseX)])
                                
def function1():
        # 1a  ##################################################################
        captureImage()

        # 1b  ##################################################################
        filename = input("Image Filename (.jpg): ")
        filename = filename + ".jpg"
        #filename = "1.jpg"
        # 1c  ##################################################################
        storeFile(filename)

        # 1d  ##################################################################
        print("\nNow select a Pixel on the Image...\n")
        global img
        img = cv2.imread('%s/%s' % (folderpath, filename))
  
        # 1e  ##################################################################
        cv2.namedWindow('Image Captured',1)
        cv2.setMouseCallback('Image Captured', get_pixel_location)
        cv2.imshow('Image Captured', img)                                        
        cv2.waitKey(0)
        cv2.destroyAllWindows()


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
        global img
        img = cv2.imread('/home/pi/Desktop/colors-copy.jpg',1)
        img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        cv2.imwrite('/home/pi/Desktop/colors-copy.jpg',img)
        
        # 3e  ##################################################################
        img1 = cv2.imread('/home/pi/Desktop/colors-copy.jpg',1)
        cv2.namedWindow('Image Captured',1)
        cv2.setMouseCallback('Image Captured', get_pixel_location)
        cv2.imshow('Image Captured', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        black = [0,0,0]
        a = img[(mouseY,mouseX)][0]
        b = img[(mouseY,mouseX)][1]
        c = img[(mouseY,mouseX)][2]
        #total = a + b + c
        
        for j in range(0,img.shape[0]):
            for i in range(0, img.shape[1]):
                blue = img[(j,i)][0]
                green = img[(j,i)][1]
                red = img[(j,i)][2]
                #othertotal = blue + green + red
                #if othertotal > total + 10 or othertotal < total - 10:
                    #img1[(j,i)] = black
                #if abs(a-blue) > 40 or abs(b-green) > 40 or abs(c-red) > 40:
                    #img[(j,i)] = black
                if blue>20 or green>200 or green<70 or red<90 or red>220:
                    img[(j,i)] = black
        # 3f  ##################################################################
        cv2.imshow('colors-copy.jpg', img1)                        
        cv2.imshow('colors-copy Yellow', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
      
function3()     
# 4   ##################################################################



# 5   ##################################################################

# 6   ##################################################################

# 7a  ##################################################################
# 7b  ##################################################################
# 7c  ##################################################################
