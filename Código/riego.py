import datetime
import time
from id import getserial
from clima import lluvia
from serial import Serial
import RPi.GPIO as GPIO
import urllib, json

#BCM -> maneja los pines por los numeros de GPIO17
#BOARD -> maneja los pines por numero de secuencia 1, 2, 3...
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

#probabilidad de lluvia
#lluvia(latitud,longitud)

#obtener serial
#getserial()

serial = getserial()
url = "http://bri2.utalca.cl/~nmaturana/getCoordenada.php?id="+serial
response = urllib.urlopen(url)
data = json.loads(response.read())
suelo = data["suelo"]

arduino = Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:
	hora = datetime.datetime.now().time()
	#Se prende desde las 6 a.m hasta las 23.59 p.m
	if (hora >= datetime.time(6,00) and hora <= datetime.time(6,20)):
		entradas = arduino.readline()
		datos = entradas.split(" ")
		if len(datos) == 2:
			humedad = datos[0]
			if humedad < 512:
				if suelo == "arena":
					#Reigo arenoso
					GPIO.output(17,GPIO.HIGH)
					time.sleep(1200)#Riego por 20 min
				else if suelo == "limoso":
					#Riego limoso
					GPIO.output(17,GPIO.HIGH)
					time.sleep(1200)#Riego por 20 min
				else:
					#Riego Arcilloso
					GPIO.output(17,GPIO.HIGH)
					time.sleep(1200)#Riego por 20 min
	else:
		GPIO.output(17,GPIO.LOW)
	time.sleep(60)

	#GPIO.output(27,GPIO.HIGH)
	#time.sleep(5)
	#GPIO.output(27,GPIO.LOW)
	#time.sleep(5)


#       hora = datetime.datetime.now().time()
        #Se prende desde las 6 a.m hasta las 23.59 p.m
#       if (hora >= datetime.time(3,00) and hora <= datetime.time(21,00)):
#               GPIO.output(17,GPIO.HIGH)
#       else:
#               GPIO.output(17,GPIO.LOW)
