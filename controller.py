import RPi.GPIO as GPIO
import sys
from time import sleep

latchPin = 13
clockPin = 15
dataPin = 11


try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup((latchPin,clockPin,dataPin), GPIO.OUT)

    def updateShiftRegister(string):
        GPIO.output(clockPin, 0)
        GPIO.output(latchPin, 0)
        GPIO.output(clockPin, 1)

        for i in range(7,-1,-1):
            GPIO.output(clockPin, 0)
            GPIO.output(dataPin, int(string[i]))
            GPIO.output(clockPin,1)
            
        GPIO.output(clockPin, 0)
        GPIO.output(latchPin, 1)
        GPIO.output(clockPin, 1)

    def path(bo):
        GPIO.output(clockPin, 0)
        GPIO.output(latchPin, 0)
        GPIO.output(clockPin, 1)

        GPIO.output(dataPin, bo)

        GPIO.output(latchPin, 1)
        sleep(1)

    def row():
        for i in range(8):
            path(1)
        for i in range(8):
            path(0)

    while True:
        row()
       # updateShiftRegister("00000000")
    #   updateShiftRegister(sys.argv[2])
            

except KeyboardInterrupt:
    updateShiftRegister("00000000")
    print("\nStopped")
finally:
    GPIO.cleanup()

