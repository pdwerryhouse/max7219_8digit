
This is a micropython library for MAX7219 + 8 x 7digit display boards.

I have tested it with an ESP8266 running micropython.

Requires a minimum of three spare GPIO lines to run SPI.


Example of use:

.. code:: python

   # Connections:
   # SCK (CLK) -> GPIO4 (D2)
   # MOSI (DIN) -> GPIO2 (D4)
   # SS (CS) -> GPIO5 (D1)
   
   from machine import Pin, SPI
   import max7219_8digit
   
   spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2), miso=Pin(0))

   ss = Pin(5, Pin.OUT)
   
   display = max7219_8digit.Display(spi, ss)
   display.write_to_buffer('12345678')
   display.display()
   

There is also a write_to_buffer_with_dots method, which attempts to use the
display decimal points properly. Note that there are some rather big bugs in
this at the moment, do not put dots at the start of the string, or put two 
of them in a row.


.. code:: python

   # Connections:
   # SCK (CLK) -> GPIO4 (D2)
   # MOSI (DIN) -> GPIO2 (D4)
   # SS (CS) -> GPIO5 (D1)
   
   from machine import Pin, SPI
   import max7219_8digit
   
   spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2), miso=Pin(0))

   ss = Pin(5, Pin.OUT)
   
   display = max7219_8digit.Display(spi, ss)
   display.write_to_buffer_with_dots('1234.56.78')
   display.display()
