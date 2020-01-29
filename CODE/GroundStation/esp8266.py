# Made by Lucas Palumbo
# Date: 1 / 26 / 2020
# Purpose: To abstarct the computer interface code from the
#          esp8266 communication code.

import serial
import logging


class esp8266Controls():

    def __init__(self):
        FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
        logging.basicConfig(format=FORMAT)
        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logger = logging.getLogger('tcpserver')
        logger.warning('Protocol problem: %s', 'connection reset', extra=d)

        self.forwardCommand = 0x00
        self.backwardsCommand = 0x01
        self.turnLeftCommand = 0x02
        self.turnRightCommand = 0x03
        self.stopCommand = 0xFF
        try:
            self.esp8266 = serial.Serial('/dev/ttyUBS0')
        except:
            pass
        #Need to add code to find find the esp8266
    # Speed can be from 0 - 255
    def forward(self, speed):
        if speed == 0:
            self.stop()
        else:
            payload  = self.forwardCommand.join(speed)
            self.esp8266.write()

    def backwards(self, speed):
        if speed == 0:
            self.stop()
        else:
            pass

    def turnLeft(self, speed):
        if speed == 0:
            self.stop()
        else:
            pass

    def turnRight(self, speed):
        if speed == 0:
            self.stop()
        else:
            pass

    def stop(self):
        pass

    def WifiSignalStrength(self):
        pass

myesp = esp8266Controls()
