#include <SoftwareSerial.h>
#include <SabertoothSimplified.h>
#include <Adafruit_NeoPixel.h>

#define FULL_SPEED 70
//Define motors
#define LEFT 2
#define RIGHT 1
#define MOTOR_PIN 6
SoftwareSerial SWSerial(NOT_A_PIN, MOTOR_PIN); // RX on no pin (unused), TX on pin 11 (to S1).
SabertoothSimplified ST(SWSerial); // Use SWSerial as the serial port.

Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 13, NEO_GRB + NEO_KHZ800);

//Input buffer for serial
char in[2] = {'a', '\0'};

void setup() {
  //Used for Motor Controler
  SWSerial.begin(9600);
  //Used for talking to the raspberry pi
  Serial.begin(115200);
  
  //Start up NEO Pixel
  strip.begin();
  strip.setPixelColor(0, 255, 0, 0);
  strip.show();
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
  strip.setBrightness(15);
  strip.setPixelColor(0, 0, 0, 0);
  strip.show();
}

void right(){
  ST.motor(RIGHT, FULL_SPEED);
  ST.motor(LEFT, -FULL_SPEED);
  strip.setPixelColor(0, 0, 255, 0);
  strip.show();
  fullStop();
}

void left(){
  ST.motor(RIGHT, -FULL_SPEED);
  ST.motor(LEFT, FULL_SPEED);
  strip.setPixelColor(0, 0, 0, 255);
  strip.show();
  fullStop();
}
