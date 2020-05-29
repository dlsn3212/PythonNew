import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)# red
GPIO.setup(20, GPIO.OUT)# green

while True:
    GPIO.output(20,True) #green on
    GPIO.output(21,False) #red off
    time.sleep(0.1)
    GPIO.output(20,False)
    GPIO.output(21,True)
    time.sleep(0.1)

#except Exception as e:
#    print(e)
#finally:
#    GPIO.cleanup()
