from time import sleep
import pifacedigitalio as pfio

pfio.init()

print 'Type: spin(rotations, speed)'

while(True):
  sleep_time = .1 / float(1)
  for loop in range(1, int(512 * float(1))):
    pfio.digital_write(4,1)
    sleep(sleep_time)
    pfio.digital_write(7,0)
    sleep(sleep_time)
    pfio.digital_write(5,1)
    sleep(sleep_time)
    pfio.digital_write(4,0)
    sleep(sleep_time)
    pfio.digital_write(6,1)
    sleep(sleep_time)
    pfio.digital_write(5,0)
    sleep(sleep_time)
    pfio.digital_write(7,1)
    sleep(sleep_time)
    pfio.digital_write(6,0)
    sleep(sleep_time)
  pfio.digital_write(7,0)
    
