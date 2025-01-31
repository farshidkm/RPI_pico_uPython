from machine import Pin
from utime import sleep_ms

led = Pin(0, mode=Pin.OUT)

while True :
    led.high()
    sleep_ms(100)
    led.low()
    sleep_ms(100)