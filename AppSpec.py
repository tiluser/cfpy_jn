'''
    Program     : AppSpec.py
    Author      : Joseph M. O'Connor
    Purpose     : Application-specific primitives - import into CreoleForth.py 
                  for use.
'''
import serial as s
import time as t

class AppSpec:
    def __init__(self):
        self.Title = "Application-specific Grouping"
        self.returnVal = 0
    
    def doTest(self, gsp):
        print("This is a testing definition - put whatever you want hee")

    def doTestOld(self, gsp):
        print("Testing definition - put whatever you want here")
        arduino = s.Serial('COM3', 115200, timeout=.1)
        #arduino.open()
        t.sleep(1) #give the connection a second to settle
        arduinoData.write('3'.encode())
        #t.sleep(1)
        """
        arduinoData.write('23'.encode())
        t.sleep(1)
        arduinoData.write('POKE'.encode())
        t.sleep(1)
        arduinoData.write('20'.encode())
        t.sleep(1)
        arduinoData.write('24'.encode())
        t.sleep(1)
        arduinoData.write('POKE'.encode())
        t.sleep(1)
        arduinoData.write('0'.encode())
        t.sleep(1)
        arduinoData.write('25'.encode())
        t.sleep(1)
        arduinoData.write('POKE'.encode())
        t.sleep(1)
        #arduino.swrite(b'20 24 POKE')
        t.sleep(1)
        """