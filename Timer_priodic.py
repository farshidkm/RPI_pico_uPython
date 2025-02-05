from machine import Pin, Timer
from utime import sleep_ms

def tim1_handle(a):
    pin1.value(not pin1.value())
    
def tim2_handle(a):
    pin2.value(not pin2.value())
    

led = Pin('LED', Pin.OUT)
pin1 = Pin(0, mode=Pin.OUT)
pin2 = Pin(1, mode=Pin.OUT)


tim1 = Timer()
tim2 = Timer()

tim1.init(mode=Timer.PERIODIC, period=1, callback=tim1_handle)
tim2.init(mode=Timer.PERIODIC, period=1, callback=tim2_handle)

while True:
    led.on()
    sleep_ms(200)
    led.off()
    sleep_ms(200)
    
    
'''
id parameter in Timer Constructor is Timer number and -1 means virtual Timer.
at this time (january 2025) hardware Timers not supported by rpi pico micropython frameware.
and id shall not be passed as a keyword argument.
RP2040’s system timer peripheral provides a global microsecond timebase and generates interrupts for it.
The software timer is available currently, and there are unlimited number of them (memory permitting).
There is no need to specify the timer id (id=-1 is supported at the moment) as it will default to this.
'''