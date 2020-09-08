import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

angle = 0.0

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# try:
while angle <=10.0:

    # print("angle = " + str(angle))
    position = angle + 2.5
    print("position = " + str(position))
    p.ChangeDutyCycle(position) # turn towards 0 degree
    time.sleep(1) # sleep
    angle = angle + 0.5
    
# except KeyboardInterrupt:
p.ChangeDutyCycle(0) 
p.stop()
GPIO.cleanup()
print("stopped and clean")