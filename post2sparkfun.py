#!/usr/bin/env python

import os
import platform
import time
import requests
# DRY :(
if platform.system() == 'Darwin':
  print "Development mode, faking DS18B20 sensor"
  from fake_DS18B20 import DS18B20
else:
  from ds18b20 import DS18B20



if __name__ == '__main__':
  sensor = DS18B20()
  
  headers = {'Phant-Private-Key': os.environ['SF_PRIVATE_KEY']}
  payload = {
      'epoch': int(time.time()),
      'temp_cel': sensor.get_temperature(),
      'temp_far': sensor.get_temperature(DS18B20.DEGREES_F)
      }
  url = "http://data.sparkfun.com/input/"+ os.environ['SF_PUBLIC_KEY']
#  print "headers:"
#  print headers
#  print "payload:"
  print payload
#  print "url"
#  print url
  r = requests.post(url, data=payload, headers=headers)
#  print "output: "
#  print r
#  print r.text
