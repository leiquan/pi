#!/usr/bin/python2
#coding=utf-8

import RPi.GPIO as GPIO
import time

def setup ():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)

def reset ():
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    
    GPIO.output(18,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)

def left_front ():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)

def right_front ():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(31,GPIO.HIGH)
    GPIO.output(33,GPIO.LOW)

def left_back ():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)

def right_back():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)

def front ():
    reset()
    left_front()
    right_front()

def back():
    reset()
    left_back()
    right_back()

def left():
    reset()
    right_front()

def right():
    reset()
    left_front()

setup()

for x in xrange(20):
    
    front()
   
    time.sleep(1)
    
    back()

    time.sleep(1)

    left()

    time.sleep(1)
    
    right()

    time.sleep(1)

GPIO.cleanup()
