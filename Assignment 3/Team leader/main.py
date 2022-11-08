print("Hello, Pi Pico!")
from machine import Pin
from utime import sleep
red = Pin(1, Pin.OUT)
yellow = Pin(5, Pin.OUT)
green = Pin(9, Pin.OUT)
while True:
  red.toggle()
  sleep(0.5)
  yellow.toggle()
  sleep(1)
  green.toggle()
  sleep(2)