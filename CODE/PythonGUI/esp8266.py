# Made by Lucas Palumbo
# Date: 1 / 26 / 2020
# Purpose: To abstarct the computer interface code from the
#          esp8266 communication code.
import sys
import serial
import glob


class esp8266Controls():

    def __init__(self):
        self.forwardCommand = 0x00
        self.backwardsCommand = 0x01
        self.turnLeftCommand = 0x02
        self.turnRightCommand = 0x03
        self.stopCommand = 0xFF
        #Algo to find the serial location of the base sation
        try:
            print(serial_ports())
            self.esp8266 = serial.Serial('/dev/ttyUBS0')
        except:
            print("FAILED TO OPEN SERIAL")
        # Need to add code to find find the esp8266

    # Speed can be from 0 - 255
    def forward(self, speed):
        if speed == 0:
            self.stop()
        else:
            payload = self.forwardCommand.join(speed)
            self.esp8266.write(payload)

    def backwards(self, speed):
        if speed == 0:
            self.stop()
        else:
            payload = self.backwardsCommand.join(speed)
            self.esp8266.write(payload)

    def turnLeft(self, speed):
        if speed == 0:
            self.stop()
        else:
            payload = self.turnLeftCommand.join(speed)
            self.esp8266.write(payload)

    def turnRight(self, speed):
        if speed == 0:
            self.stop()
        else:
            payload = self.turnRightCommand.join(speed)
            self.esp8266.write(payload)

    def stop(self):
        self.esp8266.write(0)

    def WifiSignalStrength(self):
        pass


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

myesp = esp8266Controls()
