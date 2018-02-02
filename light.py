#Author: Robert Schreibman
#Date: 2-1-18
#csci250 - Sensors
#Lab2

#Description: This code will receive light readings from the mini photocell transducer
# and store 500 readings into a numpy array

import numpy as n
from time import sleep
import spidev
import reader

adc_channel = 0
spi_channel = 0
arr = []

#we will just be calling the defined read function with a zero: (e.g., read(0)) for our lab
spi = spidev.SpiDev()                   #initiate spi object
spi.open(adc_channel, spi_channel)      #adc channel=0 (can use 1) and spi channel=0
spi.max_speed_hz = 1000000              #is 1 MHz can change the value but this worked best

for i in range(1,500):  #loop 500 times
	sleep(.001)     #sleep .001s in between light readings
	x = reader.read(0)
	#print(x)
	arr.append(x)   #append to list

print(arr)

nArray = n.array(arr)   #store data elements into numpy array





