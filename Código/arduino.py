import urllib2, urllib
from serial import Serial
import datetime
import time

arduino = Serial('/dev/ttyUSB1', 9600, timeout=1)

while True:
        hora = datetime.datetime.now()
        entradas = arduino.readline()
        datos = entradas.split(" ")
        if len(datos) == 2:
                humedad = datos[0]
                caudal = datos[1]
                print "Huemdad: " + humedad
                print "Caudal: " + caudal
        print hora
        time.sleep(5)