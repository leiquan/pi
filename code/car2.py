#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time


# 清理GPIO口
#RPi.GPIO.cleanup()

RPi.GPIO.setmode(RPi.GPIO.BCM)

# 两个电机的开和关

# 电机A,对应14口
RPi.GPIO.setup(14, RPi.GPIO.OUT)

# 电机A,对应的in1和in2
RPi.GPIO.setup(6, RPi.GPIO.OUT)
RPi.GPIO.setup(13, RPi.GPIO.OUT)

# 电机B,对应15口
RPi.GPIO.setup(15, RPi.GPIO.OUT)

# 电机B,对应的in1和in2
RPi.GPIO.setup(19, RPi.GPIO.OUT)
RPi.GPIO.setup(26, RPi.GPIO.OUT)


RPi.GPIO.output(14, True)
RPi.GPIO.output(6, False)
RPi.GPIO.output(13, True)

RPi.GPIO.output(14, True)
RPi.GPIO.output(6, True)
RPi.GPIO.output(13, False)


RPi.GPIO.cleanup()