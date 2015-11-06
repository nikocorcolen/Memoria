import urllib2, urllib
from serial import Serial
import datetime
import time

arduino = Serial('/dev/ttyUSB1', 9600, timeout=1)

while True:
	fecha = datetime.datetime.now()
	entradas = arduino.readline()
	datos = entradas.split(" ")
	if len(datos) == 2:
		humedad = datos[0]
		caudal = datos[1]
		mydata=[('humedad',humedad),('caudal',caudal),('fecha',fecha)]    #The first is the var name the second is the value
		mydata=urllib.urlencode(mydata)
		path='http://bri2.utalca.cl/~nmaturana/insertData.php'    #the url you want to POST to
		req=urllib2.Request(path, mydata)
		req.add_header("Content-type", "application/x-www-form-urlencoded")
		page=urllib2.urlopen(req).read()
		print page
		print "Huemdad: " + humedad
		print "Caudal: " + caudal
	#print fecha
	time.sleep(5)