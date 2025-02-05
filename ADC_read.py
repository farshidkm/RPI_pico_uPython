from machine import ADC, Pin
from utime import sleep_ms


pot_adc = ADC(Pin(28)) # or ADC(2)


while  True :
    pot_value_u16 = pot_adc.read_u16()
    pot_value_voltage = (pot_value_u16/65535)*3.3
    print(pot_value_voltage)
    sleep_ms(1000)
    
'''   
 ADC class Access the ADC associated with a source identified by *id*.  This
 *id* may be an integer (usually specifying a channel number), a
 :ref:`Pin <machine.Pin>` object, or other value supported by the
 underlying machine.
'''