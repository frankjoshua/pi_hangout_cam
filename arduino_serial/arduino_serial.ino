#include <SoftwareSerial.h>
#include <SabertoothSimplified.h>

#define FULL_SPEED 70
//Define motors
#define LEFT 2
#define RIGHT 1
#define MOTOR_PIN 6
SoftwareSerial SWSerial(NOT_A_PIN, MOTOR_PIN); // RX on no pin (unused), TX on pin 11 (to S1).
SabertoothSimplified ST(SWSerial); // Use SWSerial as the serial port.

//Input buffer for serial
char in[2] = {'a', '\0'};

void setup() {
  Serial.begin(115200);

}

void loop() {
  if(Serial.available() > 0){
    
   in[0] = Serial.read();
   //Serial.print(in);
   if(strcmp(in, "u") == 0){
    
   } else if(strcmp(in, "d") == 0){

   } else if(strcmp(in, "l") == 0){
      left();
   } else if(strcmp(in, "r") == 0){
      right();
   }

  }
}

void fullStop(){
  delay(500); 
  ST.motor(RIGHT, 0);
  ST.motor(LEFT, 0);
}

void right(){
  ST.motor(RIGHT, FULL_SPEED);
  ST.motor(LEFT, -FULL_SPEED);
  fullStop();
}

void left(){
  ST.motor(RIGHT, -FULL_SPEED);
  ST.motor(LEFT, FULL_SPEED);
  fullStop();
}
