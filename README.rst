
This is a micropython library for MAX7219 + 8 x 7digit display boards.

I have tested it with an ESP8266 running micropython.

Requires a minimum of three spare GPIO lines to run SPI.


Example of use:

.. code:: python

   # Connections:
   # SCK (CLK) -> GPIO4
   # MOSI (DIN) -> GPIO2
   # SS (CS) -> GPIO5
   
   from machine import Pin, SPI
   import max7219_8digit
   
   spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
   ss = Pin(5, Pin.OUT)
   
   display = max7219_8digit.Display(spi, ss)
   display.write_to_buffer('12345678')
   display.display()
   
