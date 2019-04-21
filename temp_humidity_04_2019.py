#!/usr/bin/python
import sys
from firebase import firebase
import Adafruit_DHT
from datetime import datetime, timedelta
from random import randint



i = 0
firebase = firebase.FirebaseApplication('https://raspberrypi-2019.firebaseio.com', None)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
	temp_f = temperature + randint(-5,5)
	hum_f = humidity + randint(-10,10)
	minutes_to_substract = 30 * i
	date = datetime.now() - timedelta(minutes=minutes_to_substract)
	result = firebase.post('/records', {'timestamp': date.isoformat(), 'temperature': temp_f, "humidity" : hum_f})
	i += 1

