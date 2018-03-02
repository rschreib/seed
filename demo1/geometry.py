
import math #math.degrees(math.atan(math.sqrt(3)/1))

#distance from LEDs to piCamera             D = distance   40 cm  
#horizontal distance of Left & right LEDs   L = length     44.3 pixels 
#height of lower LED to the upper LED       H = height      49.2 pixels 


#finds distance (cm) from LEDs to piCamera
def get_distance(Height): #input height of LED triangle
    Distance = 96.2* 40 / Height
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


pixels = 1270

pixel_height = 49.2

distance = get_distance(pixel_height) #49.2 pixel height of LED triangle
angle = get_angle(pixels) #pixel location from left
hypotenuse = get_distance_from_LED(pixel_height, pixels)

print "Angle:",angle
print "Distance:",distance
print "Hypotenuse:",hypotenuse




