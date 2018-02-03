#Robert Schreibman
#EENG450 SEED LAB
#Exercise 2: Intro to Open CV
#Spent 20 plus hours on this
 
#An introduction to using the pi camera and OpenCV

from picamera import PiCamera
import picamera
import picamera.array
from time import sleep
import os
import numpy as np
import cv2
import glob

#These functions should be called in numerical order in order for them to work.
#Some manual transfering of picture files into other folders may be necessary.


camera = PiCamera()
camera.rotation = 180                   #Initial Camera settings
camera.resolution = (1024, 768) 
folderpath = "/home/pi/Desktop"         
filename = "1.jpg"                      #default value

global mouseX,mouseY

def countDown():                        #Count down from 3 to 1
    for x in range(3, 0, -1):
        sleep(1)
        print(x)

def captureImage():                     #Captures image 
    print("Look into Camera ...")
    #camera.start_preview()
    countDown()
    camera.capture('%s/.image.jpg' % folderpath)
    #camera.stop_preview()

def capture(name):                      #Captures image & saves image differently
    print("Look into Camera ...")
    countDown()
    camera.capture('{}/{}.jpg'.format(folderpath,name))

def storeFile(name):                    #Create file on desktop
    os.system('mv %s/.image.jpg %s/%s' % (folderpath, folderpath, name))
    print("Succesfully created %s on Desktop" % name)

def get_pixel_location(event,x,y,flags, param):     #returns pixel location and BGR value after clicking on img
    if event == cv2.EVENT_LBUTTONDBLCLK:
            mouseX,mouseY = x,y
            print("x:",mouseX,"y:",mouseY)
            print(img[(mouseY,mouseX)])

def get_pixel_location2(event,x,y,flags, param):    #returns pixel location and BGR value after clicking on hsv
    if event == cv2.EVENT_LBUTTONDBLCLK:
            mouseX,mouseY = x,y
            print("\nx:",mouseX,"y:",mouseY)
            print(hsv[(mouseY,mouseX)])
                                
def function1():
    # 1a  ##################################################################
    captureImage()      #captures an image

    # 1b  ##################################################################
    filename = input("Image Filename (.jpg): ")   #asks the user for a filename to store the image
    filename = filename + ".jpg"

    # 1c  ##################################################################
    storeFile(filename)             # stores the captured image using the filename provided by the user

    # 1d  ##################################################################
    print("\nNow select a Pixel on the Image...\n") #displays the image on the screen
    global img
    img = cv2.imread('%s/%s' % (folderpath, filename))
  
    # 1e  ##################################################################
    cv2.namedWindow('Image Captured',1)     #asks the user to select a pixel using the mouse and displays the 3 color values for that pixel
    cv2.setMouseCallback('Image Captured', get_pixel_location)
    cv2.imshow('Image Captured', img)                                        
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def function2():    #reads a previously stored image (use an image captured from part 1), resizes 
                    #the image to half its size without changing the aspect ratio
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
    captureImage()              #captures and image

    # 3b  ##################################################################
    storeFile("colors.jpg")     #stores the image as colors.jpg
        
    # 3c  ##################################################################
                                #makes the original image smaller
    os.system('cp %s/colors.jpg %s/colors-copy.jpg' % (folderpath, folderpath))

    # 3d  ##################################################################
    global img                  #makes the original image smaller
    img = cv2.imread('/home/pi/Desktop/colors-copy.jpg',1)
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
    cv2.imwrite('/home/pi/Desktop/colors-copy.jpg',img)
        
    # 3e  ##################################################################
                                #detects the color yellow in this image
    img1 = cv2.imread('/home/pi/Desktop/colors-copy.jpg',1)
    cv2.namedWindow('Image Captured',1)
    cv2.setMouseCallback('Image Captured', get_pixel_location)
    cv2.imshow('Image Captured', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("\nProcessing Image...")

    black = [0,0,0]
    a = img[(mouseY,mouseX)][0] #image width (number of columns)
    b = img[(mouseY,mouseX)][1] #image height (number of rows)
    c = img[(mouseY,mouseX)][2] #dimension size
    
                                #loops through each pixel BGR value and changes
                                # it to black if it is not yellow
    for j in range(0,img.shape[0]):     
        for i in range(0, img.shape[1]):
            blue = img[(j,i)][0]
            green = img[(j,i)][1]
            red = img[(j,i)][2]
            if blue>45 or green>200 or green<70 or red<90 or red>220:
                 img[(j,i)] = black
                 
    # 3f  ##################################################################
                                #Display the original image and the image after the color
                                #yellow has been isolated side by side
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
                                    # makes the pixels white and black everywhere else
        yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)
                                    # adds a color tint to the white pixels
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
    # 6   ##################################################################
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

def function7():    
    # 7a  ##################################################################
    # 7b  ##################################################################
    # 7c  ##################################################################
                                #Draw contours around the blobs in the image    
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
    

    #detector = cv2.SimpleBlobDetector_create()

    external_color = [22, 255, 200]
    hole_color = 200
    max_level = 0
    keypoints = detector.detect(im)
    #im_with_contours = cv2.drawContours(im, file1Contours, external_color, hole_color,  max_level=0, thickness=1, lineType=8, offset=(0, 0))
    contours = cv.FindContours (color_mask, storage, method = cv.CV_CHAIN_APPROX_SIMPLE)
    cv2.DrawContours(img=im, contour=contours, external_color=cv.RGB(255, 0, 0), hole_color=cv.RGB(0, 255, 0), max_level=1 )
    
    #im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Contours", im_with_contours)
    #cv2.imshow("Keypoints", im_with_keypoints)
    
    ###################################################################
    '''
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
    '''
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


