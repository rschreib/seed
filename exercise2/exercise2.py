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

global mouseX,mouseY

def countDown():
    for x in range(3, 0, -1):
        sleep(1)
        print(x)

def captureImage():
    print("Look into Camera ...")
    #camera.start_preview()
    countDown()
    camera.capture('%s/.image.jpg' % folderpath)
    #camera.stop_preview()

def capture(name):
    print("Look into Camera ...")
    countDown()
    camera.capture('{}/{}.jpg'.format(folderpath,name))

def storeFile(name):
    os.system('mv %s/.image.jpg %s/%s' % (folderpath, folderpath, name))
    print("Succesfully created %s on Desktop" % name)

def get_pixel_location(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
            mouseX,mouseY = x,y
            print("x:",mouseX,"y:",mouseY)
            print(img[(mouseY,mouseX)])

def get_pixel_location2(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
            mouseX,mouseY = x,y
            print("\nx:",mouseX,"y:",mouseY)
            print(hsv[(mouseY,mouseX)])
                                
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
    print("\nProcessing Image...")

    black = [0,0,0]
    a = img[(mouseY,mouseX)][0]
    b = img[(mouseY,mouseX)][1]
    c = img[(mouseY,mouseX)][2]
        
    for j in range(0,img.shape[0]):
        for i in range(0, img.shape[1]):
            blue = img[(j,i)][0]
            green = img[(j,i)][1]
            red = img[(j,i)][2]
            #if abs(a-blue) > 40 or abs(b-green) > 40 or abs(c-red) > 40:
            if blue>45 or green>200 or green<70 or red<90 or red>220:
                 img[(j,i)] = black
                 
    # 3f  ##################################################################
    cv2.imshow('colors-copy.jpg', img1)                        
    cv2.imshow('colors-copy Yellow', img)
    print("Image Created")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def function4():
    # 4   ##################################################################
    '''
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 58
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'    #'off'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    #camera.exposure_speed = 30000 or 23000
    #camera.framerate = 30
    #camera.sharpness = 0
    '''

    lower_yellow = np.array([20,230,90])
    upper_yellow = np.array([50, 256, 245])

    lower_blue = np.array([95,210,70])
    upper_blue = np.array([140,256,250])

    lower_green = np.array([40,230,100])
    upper_green = np.array([80,256,210])

    lower_red = np.array([0,180,70])
    upper_red = np.array([15,256,241])

    pic1address = '{}/{}.jpg'.format(folderpath,'pic1')
    pic2address = '{}/{}.jpg'.format(folderpath,'pic2')
    pic3address = '{}/{}.jpg'.format(folderpath,'pic3')
    
    capture('pic1')
    capture('pic2')
    capture('pic3')
    
    p1 = cv2.imread(pic1address)
    p2 = cv2.imread(pic2address)
    p3 = cv2.imread(pic3address)
    arr = [p1,p2,p3]
    
    global hsv
    
    for i in range(3):
        p = arr[i]
        hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)

        yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)
    
        res = cv2.bitwise_and(p, p, mask= yellow_mask)
        res1 = cv2.bitwise_and(p, p, mask= blue_mask)
        res2 = cv2.bitwise_and(p, p, mask= green_mask)
        res3 = cv2.bitwise_and(p, p, mask= red_mask)

        cv2.namedWindow('pic1',1)
        cv2.setMouseCallback('pic1', get_pixel_location2)

        cv2.imshow('pic1', p)
        
        #cv2.imshow('mask', yellow_mask)
        #cv2.imshow('mask1', blue_mask)
        #cv2.imshow('mask2', green_mask)
        #cv2.imshow('mask3', red_mask)
        
        cv2.imshow('res', res)
        cv2.imshow('res1', res1)
        cv2.imshow('res2', res2)
        cv2.imshow('res3', res3)

        
        cv2.imwrite('{}/{}Y.jpg'.format(folderpath,i), res)
        cv2.imwrite('{}/{}B.jpg'.format(folderpath,i), res1)
        cv2.imwrite('{}/{}G.jpg'.format(folderpath,i), res2)
        cv2.imwrite('{}/{}R.jpg'.format(folderpath,i), res3)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def function4_5():
    file1 = '/home/pi/seed/exercise2/part4images/0B.jpg'
    file2 = '/home/pi/seed/exercise2/part4images/0G.jpg'
    file3 = '/home/pi/seed/exercise2/part4images/0R.jpg'
    file4 = '/home/pi/seed/exercise2/part4images/0Y.jpg'

    img1 = cv2.imread(file1, 0)
    img2 = cv2.imread(file2, 0)
    img3 = cv2.imread(file3, 0)
    img4 = cv2.imread(file4, 0)

    combined = np.array([(img1[i] + img2[i] + img3[i] + img4[i]) for i in range(img1.shape[0])])
   
    file5 = '/home/pi/seed/exercise2/part4images/Combined.jpg'

    cv2.imshow('Combined Image', combined)
    cv2.imwrite(file5, combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def function5():
    # 5   ##################################################################
    file1 = '/home/pi/seed/exercise2/part5/Combined.jpg'
    file1new = '/home/pi/seed/exercise2/part5/Combinednew.jpg'
    img = cv2.imread(file1,0)
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    erosion = cv2.erode(opening,kernel,iterations = 2)
    #closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    #dilation = cv2.dilate(img2,kernel,iterations = 1)

    cv2.imshow('Morphed Image', erosion)
    cv2.imwrite(file1new, erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def function6():
    # 6   ##################################################################
    file1 = '/home/pi/seed/exercise2/part5/Combinednew.jpg'
    file1blurred = '/home/pi/seed/exercise2/part6/CombinednewBlurred.jpg'
    img = cv2.imread(file1,0)
    
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow('Gray Image', blur)
    cv2.imwrite(file1blurred, blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def function7():
  
    
    # 7a  ##################################################################


    # 7b  ##################################################################
    # 7c  ##################################################################
