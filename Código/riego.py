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
	fecha = datetime.datetime.now()
	entradas = arduino.readline()
	datos = entradas.split(" ")
	if len(datos) == 2:
		humedad = datos[0]
		caudal = datos[1]
		#suelo
	#GPIO.output(27,GPIO.HIGH)
	#time.sleep(5)
	#GPIO.output(27,GPIO.LOW)
	#time.sleep(5)