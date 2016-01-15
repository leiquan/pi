#!/usr/bin/env python

"""
可以正常运行的代码
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(11, True)

    time.sleep(1)
    GPIO.output(11, False)
    time.sleep(1)
