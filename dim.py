#!/usr/bin/python
import RPi.GPIO as GPIO
import os,signal,sys

PIN = 8
LIGHT_PERCENTAGE = 0.75
FREQUENCY = 0.02
light_time = FREQUENCY * LIGHT_PERCENTAGE
off_time = FREQUENCY - light_time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

def sigterm_handler(signal, frame):
  print "got SIGTERM"
  GPIO.output(PIN,GPIO.LOW)
  sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

while True:
  GPIO.output(PIN,GPIO.HIGH)
  time.sleep(light_time)
  GPIO.output(PIN,GPIO.LOW)
  time.sleep(off_time)
