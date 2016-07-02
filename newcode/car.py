#!/usr/bin/python2
#coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


def clean_and_setup ():
    
    GPIO.cleanup()
    
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)


def front():

    while (True):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)

        GPIO.output(18,GPIO.HIGH)
        GPIO.output(31,GPIO.HIGH)
        GPIO.output(33,GPIO.LOW)


def back():
    
    while (True):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)

        GPIO.output(18,GPIO.HIGH)
        GPIO.output(31,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)


for x in xrange(5):
    
    clean_and_setup()
    front()
    time.sleep(2);
    
    clean_and_setup()
    back()
    time.sleep(2)
