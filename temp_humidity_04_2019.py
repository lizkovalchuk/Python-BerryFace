#!/usr/bin/python
import sys
from firebase import firebase
import Adafruit_DHT
from datetime import datetime, timedelta

firebase = firebase.FirebaseApplication('https://raspberrypi-2019.firebaseio.com', None)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
	temp_f = temperature
	hum_f = humidity
	date = datetime.now()
	firebase.post('/records', {'timestamp': date.isoformat(), 'temperature': temp_f, "humidity" : hum_f})
	sys.exit()