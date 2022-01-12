import RPi.GPIO as GPIO
from time import sleep

servoPIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) #Pin 11 for PWM with 50hz
p.start(2.5) #Initialization

def move(degree, time):
    p.ChangeDutyCycle(degree)
    sleep(time)

try:
    while True:
        move(5, 1)
        move(7.5, 1)
        move(10, 1)
        move(12.5, 2)
        move(10, 1)
        move(7.5, 1)
        move(5, 1)
        move(2.5, 1)
        '''
        p.ChangeDutyCycle(5)
        sleep(1)
        p.ChangeDutyCycle(7.5)
        sleep(1)
        p.ChangeDutyCycle(10)
        sleep(1)
        p.ChangeDutyCycle(12.5)
        sleep(1)
        p.ChangeDutyCycle(10)
        sleep(1)
        p.ChangeDutyCycle(7.5)
        sleep(1)
        p.ChangeDutyCycle(5)
        sleep(1)
        p.ChangeDutyCycle(2.5)
        sleep(1)
        '''
except KeyboardInterrupt: #ctrl+c
    p.ChangeDutyCycle(2.5)
    sleep(1)
    p.stop()
    print("\nStopped")
finally:
    GPIO.cleanup()
