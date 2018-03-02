#Robert Schreibman
#EENG450 SEED LAB
#Mini Project: Intro to Open CV

from time import sleep

import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob
import warnings
warnings.filterwarnings('ignore')


camera = PiCamera()
camera.iso = 100
camera.rotation = 180                   
camera.resolution = (512, 380)


folderpath = "/home/pi/seed/miniProject"
filename = "image"
mouseX = 0
mouseY = 0

def captureImage(folderpath,name):      #Captures image & saves image to file
    print("Look into Camera ...")
    for x in range(3, 0, -1):
        sleep(.2)
        print(x)
    camera.capture('{}/{}.jpg'.format(folderpath,name))
    print("Succesfully created %s on Desktop" % name)

def get_pixel_location(event,x,y,flags, param):     #returns pixel location, BGR, & HSV value after double clicking on img
    if event == cv2.EVENT_LBUTTONDBLCLK:
            global mouseX, mouseY
            mouseX,mouseY = x,y
            print("x:",mouseX,"y:",mouseY)
            print("BGR: ", img[(mouseY,mouseX)])
            print("HSV: ", hsv_img[(mouseY,mouseX)])
            print("")

lower_green = np.array([40,230,100])
upper_green = np.array([80,256,210])

lower_red = np.array([0,180,70])
upper_red = np.array([15,256,241])

pic1address = '{}/{}.jpg'.format(folderpath,'pic1')

for i in range(2):
    capture('pic1')
    
    p = cv2.imread(pic1address)
    
    global hsv
    
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
                                    # makes the pixels white and black everywhere else
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
                                    # adds a color tint to the white pixels
    res2 = cv2.bitwise_and(p, p, mask= green_mask)
    res3 = cv2.bitwise_and(p, p, mask= red_mask)

    cv2.namedWindow('pic1',1)
    cv2.setMouseCallback('pic1', get_pixel_location2)

    cv2.imwrite('{}/G.jpg'.format(folderpath), res2)
    cv2.imwrite('{}/R.jpg'.format(folderpath), res3)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()


