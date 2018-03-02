import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob
import math

#finds distance (cm) from LEDs to piCamera
def get_distance(Height): #input height of LED triangle
    Distance = 96.2*40/Height
    return Distance

#38, 21.5 (adjacent, opposite) (used to calculate camera angle)
#total degrees of range is -30 (left) +30 (right) or use -29.5 & +29.5
def get_angle(LED_pixel_X): #input the x value of one of the LED Pixels (or center of triangle pixel)
    pixel_middle_of_screen_X = 640.0
    max_camera_angle = 30.0
    #approximate angle
    angle = (LED_pixel_X - pixel_middle_of_screen_X) / pixel_middle_of_screen_X * max_camera_angle
    return angle

#Inputs: LED triangle pixel Height, LED pixel location from left of screen
def get_distance_from_LED(Height, LED_pixel_X):
    angle = get_angle(LED_pixel_X)
    distance = get_distance(Height)
    hypotenuse = distance / math.cos(math.radians(angle))
    return hypotenuse

def detect(camera, run):
    prev = run
    rawCapture = PiRGBArray(camera)
    camera.iso = 100
    camera.shutter_speed = 1800

    camera.capture(rawCapture, format="bgr")
    img = rawCapture.array

    cv2.imwrite('led.jpg',img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,10,200])
    upper_red = np.array([175, 50, 255])
    mask_red = cv2.inRange(hsv,lower_red,upper_red)

    lower_blue = np.array([100,10,200])
    upper_blue = np.array([125, 50, 255])
    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)

    lower_green = np.array([50,10,200])
    upper_green = np.array([80, 50, 255])
    mask_green = cv2.inRange(hsv,lower_green,upper_green)

    kernal = np.ones((5,5),np.uint8)
    #mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernal)
    mask_red = cv2.dilate(mask_red,kernal,iterations=2)
    mask_blue = cv2.dilate(mask_blue,kernal,iterations=2)
    mask_green = cv2.dilate(mask_green,kernal,iterations=2)
    #mask = cv2.erode(mask,kernal,iterations=1)

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 20;
    params.maxThreshold = 200;

    params.filterByArea = False
    params.minArea = .1

    params.filterByColor= False
    params.blobColor = 200

    params.filterByCircularity = False
    params.minCircularity = 0.1

    params.filterByConvexity = False
    params.minConvexity = 0.5

    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    mask = cv2.bitwise_or(mask_red, mask_blue)
    mask = cv2.bitwise_or(mask, mask_green)
    #cv2.imshow('image', img)
    #cv2.imshow('mask', mask)

    img1 = cv2.resize(img,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
    mask = cv2.resize(mask,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
    cv2.imshow('image',img1)
    cv2.imshow('mask',mask)

    detector = cv2.SimpleBlobDetector(params)
    keypoints_red = detector.detect(mask_red)
    keypoints_blue = detector.detect(mask_blue)
    keypoints_green = detector.detect(mask_green)
    keypoints = []
    try:
        keypoints.append(keypoints_red[0])
    except:
        print "Red LED not found"
    try:
        keypoints.append(keypoints_blue[0])
    except:
        print 'Blue LED not found'
    try:
        keypoints.append(keypoints_green[0])
    except:
        print 'Green LED not found'

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return keypoints
    

camera = PiCamera(resolution=(1280,640))
run = False

#camera.exposure_mode = 'off'
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g
time.sleep(1)

#detect(camera,run)

keypoints = detect(camera,run)

LED_pixel_X = keypoints[2].pt[0]
triangle_pixel_height = keypoints[0].pt[1]-keypoints[2].pt[1]

angle = get_angle(LED_pixel_X) #pixel 160 from left
distance = get_distance(triangle_pixel_height) #49.2 pixel height of LED triangle
hypotenuse = get_distance_from_LED(triangle_pixel_height, LED_pixel_X)

print 'Height:',triangle_pixel_height
print "Angle:",angle, 'degrees'
print "Distance:",distance, 'cm'
print "Hypotenuse:",hypotenuse,'cm'

