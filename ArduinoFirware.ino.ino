#include<SoftwareSerial.h>

SoftwareSerial mySerial(0, 1); //black, red

void setup(){
  Serial.begin(9600);
  mySerial.begin(115200);
}

void loop(){
  String msg = mySerial.readStringUntil('\r');
Serial.println(msg);
}
