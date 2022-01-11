import RPi.GPIO as GPIO
from time import sleep

try:
    RED = 8
    GREEN = 12
    YELLOW = 11

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
        
    GPIO.setup(RED, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(GREEN, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(YELLOW, GPIO.OUT, initial = GPIO.HIGH)

    def led_on(color):
        GPIO.output(color, GPIO.HIGH)

    def led_off(color):
        GPIO.output(color, GPIO.LOW)
        
    def pauseTicker(pause):
        for i in range(pause):
            if i % 2 == 0:
                GPIO.output(YELLOW, GPIO.HIGH)
                sleep(1)
            else:
                GPIO.output(YELLOW, GPIO.LOW)
                sleep(1)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
        sleep(1)

    GPIO.output(YELLOW, GPIO.LOW)
    sleep(5)

        
    while True:
        led_on(GREEN)
        led_off(RED)
        pauseTicker(15)
        led_on(RED)
        led_off(GREEN)
        pauseTicker(15)
except KeyboardInterrupt:
    print("Stopped")
finally:
    GPIO.cleanup()