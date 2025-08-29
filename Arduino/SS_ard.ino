#include <Wire.h>

uint8_t pir[] = { 4, 5, 6, 7 };
uint8_t code;

byte i2c_rcv;
unsigned long time_start;
int stat_LED;

void setup() {
  Wire.begin(0x08);
  Wire.onReceive(dataRcv);
  Wire.onRequest(dataRqst);

  Serial.begin(9600);

  for (uint8_t i=0;i<4;i++){
    pinMode(pir[i], INPUT);
  }

  i2c_rcv = 255;
  time_start = millis();
  stat_LED = 0;
  pinMode(13, OUTPUT);
}

void loop() {
  if ((millis() - time_start) > (1000 * (float)(i2c_rcv / 255))) {
    stat_LED = !stat_LED;
    time_start = millis();
    digitalWrite(13, stat_LED);
  }
}


void dataRcv(int numBytes) {
  uint8_t counter = 0;
  uint8_t data[] = { 0, 0, 0, 0 };
  while (Wire.available()) {  // read all bytes received
    code = Wire.read();
    Serial.print("Get code: ");
    Serial.println(code);
  }
}

// requests data handler function
void dataRqst() {
  Wire.write(digitalRead(pir[code]));  // send potentiometer position
  Serial.println(digitalRead(pir[code]));
}
