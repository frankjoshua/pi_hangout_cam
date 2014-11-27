#include <Servo.h>

//Setup servos
Servo tiltServo;
#define PIN_TILT_SERVO 8
Servo panServo;
#define PIN_PAN_SERVO 7

//Input budder for serial
char in[2] = {'a', '\0'};

#define STEPS 15
#define MAX_PAN 165
#define MAX_TILT 165
#define MIN_PAN 15
#define MIN_TILT 15

int mTilt = 90;
int mPan = 90;

void setup() {
  Serial.begin(115200);
  tiltServo.attach(PIN_TILT_SERVO);
  tiltServo.write(mTilt);
  panServo.attach(PIN_PAN_SERVO);
  panServo.write(mPan);
}

void loop() {
  if(Serial.available() > 0){
    
   in[0] = Serial.read();
   //Serial.print(in);
   if(strcmp(in, "u") == 0){
     mTilt += STEPS;
   } else if(strcmp(in, "d") == 0){
     mTilt -= STEPS;
   } else if(strcmp(in, "l") == 0){
     mPan += STEPS;
   } else if(strcmp(in, "r") == 0){
     mPan -= STEPS;
   }
   //Check for out of range values
   if(mTilt > MAX_TILT){
     mTilt -= STEPS;
   } else if(mTilt < MIN_TILT){
     mTilt += STEPS; 
   }
   if(mPan > MAX_PAN){
     mPan -= STEPS; 
   } else if(mPan < MIN_PAN){
     mPan += STEPS; 
   }
   //Move servos
   tiltServo.write(mTilt);
   panServo.write(mPan);
  }
}
