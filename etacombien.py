#!/usr/bin/env python
from flask import Flask,render_template
from flask_bootstrap import Bootstrap

import platform

if platform.system() == 'Darwin':
  print "Development mode, faking DS18B20 sensor"
  from fake_DS18B20 import DS18B20
else:
  from ds18b20 import DS18B20

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  app.config['BOOTSTRAP_SERVE_LOCAL'] = True
  sensor = DS18B20()

  def read_celsius():
    return sensor.get_temperature()

  def read_fahrenheit():
    return sensor.get_temperature(DS18B20.DEGREES_F)

  @app.route("/temp/celsius")
  def celsius():
    return "%s" % read_celsius()

  @app.route("/temp/fahrenheit")
  def fahrenheit():
    return "%s" % read_fahrenheit()

  @app.route("/")
  def index():
    celsius = read_celsius()
    fahrenheit = read_fahrenheit()
    return render_template('index.html', celsius=celsius, fahrenheit=fahrenheit)

  return app

if __name__ == '__main__':
  create_app().run(debug=True, host='0.0.0.0')
