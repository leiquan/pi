#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time


RPi.GPIO.setmode(RPi.GPIO.BCM)

n=14
RPi.GPIO.setup(n, RPi.GPIO.OUT)
RPi.GPIO.output(n, True)
