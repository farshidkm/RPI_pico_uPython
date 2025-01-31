from machine import Pin
from utime import sleep_ms

key = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)

while True :
    print(key.value())
    sleep_ms(1000)
    