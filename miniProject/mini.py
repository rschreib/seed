#Robert Schreibman
#EENG450 SEED LAB
#Exercise 2: Intro to Open CV

from picamera import PiCamera
import picamera
import picamera.array
from time import sleep
import os
import numpy as np
import cv2
import glob

camera = PiCamera()
camera.rotation = 180                   
camera.resolution = (1024, 768) 
folderpath = "/home/pi/Desktop"         
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
 
def function1():
    captureImage(folderpath,filename)              #captures and image
    global img
    global hsv_img   

    img = cv2.imread('{}/{}.jpg'.format(folderpath,filename),1)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    cv2.namedWindow('Image Captured',1)
    cv2.setMouseCallback('Image Captured', get_pixel_location)
    cv2.imshow('Image Captured', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   ''' 
    print("Processing Image...")
    black = [0,0,0]
    print(mouseX,mouseY)
    a = img[mouseY,mouseX][0] 
    b = img[mouseY,mouseX][1] 
    c = img[mouseY,mouseX][2] 
     
    adjusted_img = img
    
    for j in range(img.shape[0]):         #image width (number of columns)
        for i in range(img.shape[1]):    #image height (number of rows) # shape[2] = dimension size
            blue = img[(j,i)][0]
            green = img[(j,i)][1]
            red = img[(j,i)][2]
            
            if abs(blue-a) > 30 or abs(green-b) > 30 or abs(red-c) > 30:
                adjusted_img[(j,i)] = black               
    '''              
    hsv_img = cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2HSV)
    
    cv2.namedWindow('Image Captured',1)
    cv2.setMouseCallback('Image Captured', get_pixel_location)
    cv2.imshow('Image Captured', adjusted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

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
    #Takes three pictures (using the Pi Camera) of the colors slide in different lighting
    #conditions, at different distances and at different heights. Changes the images
    #from BGR to the HSV color space. Isolates yellow, blue,
    #green, and red in all of these images

                    #Define ranges for the pixel colors
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
    #capture('pic2')
    #capture('pic3')
    
    p = cv2.imread(pic1address)
    #p2 = cv2.imread(pic2address)
    #p3 = cv2.imread(pic3address)
    #arr = [p1,p2,p3]
    
    global hsv
    
    #for i in range(3):
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
                                    # makes the pixels white and black everywhere else
        #yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        #blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
                                    # adds a color tint to the white pixels
        #res = cv2.bitwise_and(p, p, mask= yellow_mask)
        #res1 = cv2.bitwise_and(p, p, mask= blue_mask)
    res2 = cv2.bitwise_and(p, p, mask= green_mask)
    res3 = cv2.bitwise_and(p, p, mask= red_mask)

    cv2.namedWindow('pic1',1)
    cv2.setMouseCallback('pic1', get_pixel_location2)

    cv2.imshow('pic1', p)
        
        #cv2.imshow('mask', yellow_mask)
        #cv2.imshow('mask1', blue_mask)
    #cv2.imshow('mask2', green_mask)
    #cv2.imshow('mask3', red_mask)
        
        #cv2.imshow('res', res)
        #cv2.imshow('res1', res1)
    cv2.imshow('res2', res2)
    cv2.imshow('res3', res3)
        
        #cv2.imwrite('{}/{}Y.jpg'.format(folderpath,i), res)
        #cv2.imwrite('{}/{}B.jpg'.format(folderpath,i), res1)
    cv2.imwrite('{}/{}G.jpg'.format(folderpath,i), res2)
    cv2.imwrite('{}/{}R.jpg'.format(folderpath,i), res3)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()



function1() 
def function4_5():
    # This will take 4 of the isolated colored images and combine them into one image by
    # adding the numpy.arrays together using matrix addition
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
                                #Cleans up the image by performing morphological transformations.
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
                                #Convert the cleaned-up image to a grayscale image
    file1 = '/home/pi/seed/exercise2/part5/Combinednew.jpg'
    file1blurred = '/home/pi/seed/exercise2/part6/CombinednewBlurred.jpg'
    img = cv2.imread(file1,0)
    
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                #Blurs the image a little bit
    blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow('Gray Image', blur)
    cv2.imwrite(file1blurred, blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''    
def function7():    
    file1 = '/home/pi/seed/exercise2/part6/CombinednewBlurred.jpg'
    file1Contours = '/home/pi/seed/exercise2/part6/CombinednewBlurredCountours.jpg'
    im = cv2.imread(file1, 0)
    ########################################################################
    
    # Setup SimpleBlobDetector parameters.
    
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 10;
    params.maxThreshold = 200;

    # Filter by Color
    params.filterByColor = True
    params.blobColor = 150
     
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 50
    params.maxArea = 2000
     
    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1
     
    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.17
     
    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01
     
    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
    
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # define range of purple color in HSV
    purpleMin = (115,50,10)
    purpleMax = (160, 255, 255)
    # Sets pixels to white if in purple range, else will be set to black
    mask = cv2.inRange(hsv, purpleMin, purpleMax)
        
    # Bitwise-AND of mask and purple only image - only used for display
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # Set up the SimpleBlobdetector with default parameters.
    params = cv2.SimpleBlobDetector_Params()
     
    # Change thresholds
    params.minThreshold = 0;
    params.maxThreshold = 256;
     
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 30
     
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
     
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.5
     
    # Filter by Inertia
    params.filterByInertia =True
    params.minInertiaRatio = 0.5
     
    detector = cv2.SimpleBlobDetector_create(params)
 
    # Detect blobs.
    reversemask=255-mask
    keypoints = detector.detect(reversemask)

    cv2.imshow("Blob", keypoints)
    
    cv2.waitKey(0)
    '''
