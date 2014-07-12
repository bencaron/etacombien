#!/usr/bin/env python
from flask import Flask,render_template
from flask_bootstrap import Bootstrap

import os

if os.environ.get('DEV'):
  from fake_DS18B20 import DS18B20
else:
  from ds18b20 import DS18B20

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  sensor = DS18B20()

  def read_celcius():
    return sensor.get_temperature()

  def read_farenheit():
    return sensor.get_temperature(DS18B20.DEGREES_F)

  @app.route("/temp/celcius")
  def celcius():
    return "%s" % read_celcius()

  @app.route("/temp/farenheit")
  def farenheit():
    return "%s" % read_farenheit()

  @app.route("/")
  def index():
    celcius = read_celcius()
    farenheit = read_farenheit()
    return render_template('index.html', celcius=celcius, farenheit=farenheit)

  return app

if __name__ == '__main__':
  create_app().run(debug=True)
