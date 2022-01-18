import RPi.GPIO as GPIO
import time

# declare pin layout
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)

mode = GPIO.getmode()
print(mode)

# setup channel
chan_list = [12]
# GPIO.setup(channel, GPIO.IN)
# GPIO.setup(chan_list, GPIO.OUT)
# initial value
# GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.HIGH)
print("setup channel 79 to out and high")

time.sleep(30)
print("cleaning up the channels")
GPIO.cleanup()
