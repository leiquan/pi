#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: darkbull
# @Date:   2014-05-31 10:02:21
# @Last Modified by:   darkbull
# @Last Modified time: 2014-06-02 15:29:20

"""Web控制树莓派小车
"""


#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.output(37, False)

# 左边轮速度控制
PWM_L = 37
PWM_R = 38

pwm_l = GPIO.PWM(PWM_L, 50)
pwm_r = GPIO.PWM(PWM_R, 50)

pwm_l.start(50)
pwm_r.start(50) 
