#include <Wire.h>

uint8_t pir[] = { 2, 3, 4, 5, 6, 7, 8, 9 };

void setup() {
  Serial.begin(9600);

  for (uint8_t i=0;i<8;i++){
    pinMode(pir[i], INPUT);
  }


}

void loop() {

  if (Serial.available()){
    int code = Serial.read() - '0';
    Serial.println(digitalRead(pir[code]));
  }
}


