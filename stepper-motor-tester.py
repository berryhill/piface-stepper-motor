from time import sleep
import pifacedigitalio as pfio

pfio.init()

print 'Type: spin(rotations, speed)'

while(True):
  sleep_time = .1 / 1
  pfio.digital_write(1,1)
  pfio.digital_write(2,0)
  pfio.digital_write(3,0)
  sleep(sleep_time)
  pfio.digital_write(2,1)
  pfio.digital_write(1,0)
  pfio.digital_write(3,0)
  sleep(sleep_time)
  pfio.digital_write(3,1)
  pfio.digital_write(1,0)
  pfio.digital_write(2,0)
  sleep(sleep_time)
    
