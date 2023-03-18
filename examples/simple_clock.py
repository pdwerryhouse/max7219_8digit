from machine import RTC
import time
from machine import Pin, SoftSPI
import max7219_8digit

days = ['' 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def start():
  spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2), miso=Pin(0))
  ss = Pin(5, Pin.OUT)
  display = max7219_8digit.Display(spi, ss)

  rtc = RTC()

  while True:
    (year,month,day,weekday,hour,minute,second,_) = rtc.datetime()
    date_s = "%04d %03s" % (year, days[weekday])
    display.write_to_buffer(date_s)
    display.display()
    time.sleep(3)

    (year,month,day,weekday,hour,minute,second,_) = rtc.datetime()
    date_s = "%03s %02s" % (months[month], day)
    display.write_to_buffer(date_s)
    display.display()
    time.sleep(3)

    (year,month,day,weekday,hour,minute,second,_) = rtc.datetime()
    time_s = "%02d %02d %02d" % (hour, minute, second)
    display.write_to_buffer(time_s)
    display.display()
    time.sleep(3)
