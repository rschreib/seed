from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

def prev():
    #camera.start_preview(alpha=100) #alpha refers to level of transparency
    #sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    #camera.stop_preview()

def photoburst():
    camera.annotate_text = "hello world!"
    camera.brightness = 70  #[0,100] default 50
    camera.start_preview(alpha=100)  
    for i in range(1):
        sleep(3)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)                   
    camera.stop_preview()

def photobrightness():
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()

def video(): #run video in terminal "omxplayer video.h264"
    camera.resolution = (64, 64) #max res
    camera.framerate = 15 #15 is max rate
    camera.start_preview(alpha=100)
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(6)
    camera.stop_recording()
    camera.stop_preview()


prev()

