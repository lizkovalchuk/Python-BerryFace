#!/usr/bin/python
import sys
from firebase import firebase
import Adafruit_DHT
from datetime import datetime

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

firebase = firebase.FirebaseApplication('https://raspberrypi-2019.firebaseio.com', None)
result = firebase.post('/temperatures', temperature)
result = firebase.post('/humidity', {'value': humidity, 'time': datetime.now().isoformat()})
print result
