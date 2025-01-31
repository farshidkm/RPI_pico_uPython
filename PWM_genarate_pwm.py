from machine import Pin, PWM

pwm = PWM(Pin(0))

pwm.freq(10_000)
pwm.duty_u16(16_000)


'''

   Limitations of PWM
   ------------------
   
   * Not all frequencies can be generated with absolute accuracy due to
     the discrete nature of the computing hardware.  Typically the PWM frequency
     is obtained by dividing some integer base frequency by an integer divider.
     For example, if the base frequency is 80MHz and the required PWM frequency is
     300kHz the divider must be a non-integer number 80000000 / 300000 = 266.67.
     After rounding the divider is set to 267 and the PWM frequency will be
     80000000 / 267 = 299625.5 Hz, not 300kHz.  If the divider is set to 266 then
     the PWM frequency will be 80000000 / 266 = 300751.9 Hz, but again not 300kHz.
   
   * The duty cycle has the same discrete nature and its absolute accuracy is not
     achievable.  On most hardware platforms the duty will be applied at the next
     frequency period.  Therefore, you should wait more than "1/frequency" before
     measuring the duty.
   
   * The frequency and the duty cycle resolution are usually interdependent.
     The higher the PWM frequency the lower the duty resolution which is available,
     and vice versa. For example, a 300kHz PWM frequency can have a duty cycle
     resolution of 8 bit, not 16-bit as may be expected.  In this case, the lowest
     8 bits of *duty_u16* are insignificant. So::
   
       pwm=PWM(Pin(13), freq=300_000, duty_u16=2**16//2)
   
     and::
   
       pwm=PWM(Pin(13), freq=300_000, duty_u16=2**16//2 + 255)
   
     will generate PWM with the same 50% duty cycle.
'''
