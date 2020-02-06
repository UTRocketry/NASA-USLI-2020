#!/usr/bin/env python

from .esp8266 import esp8266

myesp = esp8266()

myesp.forward()
myesp.backwards()
myesp.stop()
