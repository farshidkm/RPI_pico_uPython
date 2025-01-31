from machine import Pin
from utime import sleep_ms

key = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)

def key_interrupt_handler(pin):
    print('external interrupt occured')
    
    

key.irq(handler=key_interrupt_handler, trigger=Pin.IRQ_FALLING)

while True :
    pass