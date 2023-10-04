import serial
import time
import RPi.GPIO as GPIO

LEDpin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LEDpin,GPIO.OUT)
GPIO.output(LEDpin,GPIO.LOW)
Dist_Total = 0
ser = serial.Serial('/dev/serial0',115200,timeout = 1)

##ser.write(str(0x42))
ser.write(bytes(b'B'))

#ser.write(0x57)
ser.write(bytes(b'W'))

#ser.write(0x02)
ser.write(bytes(2))

#ser.write(0x00)
ser.write(bytes(0))

#ser.write(0x00)
ser.write(bytes(0))

#ser.write(0x00)
ser.write(bytes(0))
          
#ser.write(0x01)
ser.write(bytes(1))
          
#ser.write(0x06)
ser.write(bytes(6))

while(True):
    while(ser.in_waiting >= 9):
##        print (ser.read())
        if(('Y' == ser.read()) and ( 'Y' == ser.read())):
            
            GPIO.output(LEDpin, GPIO.LOW)
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
            for i in range (0,5):
                ser.read()
                
        print(Dist_Total)
        time.sleep(1)


        
