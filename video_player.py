# External module imports
import time
import RPi.GPIO as GPIO
import sys
import os
import subprocess
from subprocess import Popen
#import pygame


#ignores GPIO errors
GPIO.setwarnings(False)

# Pin Definitons

#LED assignment
buttonLed4 = 22
buttonLed3 = 23
buttonLed2 = 20
buttonLed1 = 21 

#button assignment
button4 = 12 
button3 = 13 
button2 = 16 
button1 = 17 

# Pin Setup
# Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BCM) 

# LED pin set as output
GPIO.setup(buttonLed1, GPIO.OUT) 
GPIO.setup(buttonLed2, GPIO.OUT) 
GPIO.setup(buttonLed3, GPIO.OUT) 
GPIO.setup(buttonLed4, GPIO.OUT) 

# Button pin set as input with pull-up
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initial state for LEDs
GPIO.output(buttonLed1, GPIO.LOW)
GPIO.output(buttonLed2, GPIO.LOW)
GPIO.output(buttonLed3, GPIO.LOW)
GPIO.output(buttonLed4, GPIO.LOW)

# Video assignment
movie1 = '/home/pi/code/video/1.mov'
movie2 = '/home/pi/code/video/2.mov'
movie3 = '/home/pi/code/video/3.mov'
movie4 = '/home/pi/code/video/4.mov'
movie5 = '/home/pi/code/video/splash.mov'

#kills any active instance of OMXplayer on start
os.system('killall omxplayer.bin')

#this is what process it is looking for is running
process_name= "omxplayer.bin" 

#Uses pygame to hide desktop
#Prevents user killing the process
#screen = pygame.display.set_mode((1024, 768), pygame.NOFRAME)
#pygame.mouse.set_visible(False)



while True:
#varible to store if omxplayer is running
	tmp = os.popen("ps -Af").read()

	if GPIO.input(button1):
		time.sleep(.01)
	else:
		GPIO.output(buttonLed1, GPIO.HIGH)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(1)
		omxp = Popen(['omxplayer','-o','local',movie1])
		time.sleep(1)		
	if GPIO.input(button2):		
		time.sleep(.01)		
	else:
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.HIGH)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(1)
		omxp = Popen(['omxplayer','-o','local',movie2])
		time.sleep(1)
	if GPIO.input(button3):		
		time.sleep(.01)		
	else:
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.HIGH)
		GPIO.output(buttonLed4, GPIO.LOW)
		os.system('killall omxplayer.bin')
		time.sleep(1)
		omxp = Popen(['omxplayer','-o','local',movie3])
		time.sleep(1)		
	if GPIO.input(button4):
		time.sleep(.01)		
	else:		
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.HIGH)
		os.system('killall omxplayer.bin')
		time.sleep(1)
		omxp = Popen(['omxplayer','-o','local',movie4])
		time.sleep(1)
	if process_name not in tmp[:]:		 
		time.sleep(.01)
		GPIO.output(buttonLed1, GPIO.LOW)
		GPIO.output(buttonLed2, GPIO.LOW)
		GPIO.output(buttonLed3, GPIO.LOW)
		GPIO.output(buttonLed4, GPIO.LOW)
		omxp = Popen(['omxplayer',movie5])
		time.sleep(1)
	
				
	

			
time.sleep(.01)	

	
	


