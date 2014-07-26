import random
class DS18B20():
  DEGREES_F = 2
  def get_temperature(self, celcius=1):
    if celcius == 1:
      return random.randrange(2333, 2611) / 100.0
    else:
      return random.randrange(7500, 7900) / 100.0

