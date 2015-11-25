volatile int  frecuencia_sensor;  // Mide los pulsos de flujo
unsigned int  litrosHora;          // Calcula los litros por hora  
unsigned int humedad_sensor;        // Mide la humedad del suelo                    
unsigned char pinFlujo = 2;  // Pin de flujo
unsigned char pinHumedad = A0;  // Pin de humedad
unsigned long tiempoActual;
unsigned long tiempoCiclo;

void flujo ()                  // Interruot function
{ 
  frecuencia_sensor++;
}

void setup() {
  pinMode(pinFlujo, INPUT);
  Serial.begin(9600); 
  attachInterrupt(0, flujo, RISING); // Setup Interrupt 
  sei();                            // Enable interrupts  
  tiempoActual = millis();
  tiempoCiclo = tiempoActual;
}

void loop() {
  humedad_sensor = analogRead(pinHumedad);
  //Serial.print(humedad_sensor);
  //Serial.println(" Humedad");
  tiempoActual = millis();
  //Cada segundo, calcula e imprime litros por hora
  if(tiempoActual >= (tiempoCiclo + 1000))
  {     
    tiempoCiclo = tiempoActual;              // Actualiza tiempoCiclo
    litrosHora = (frecuencia_sensor * 60 / 7.5); // (Pulse frequency x 60 min) / 7.5Q = L/hour 
    frecuencia_sensor = 0;                   // Resetea el contador
    //Serial.print(litrosHora);            // Imprime litro por hora
    //Serial.println(" L/hour");
    //Serial.print(humedad_sensor);
    //Serial.println(" Humedad");
    Serial.println(String(humedad_sensor) + " " + String(litrosHora));
  }
}

