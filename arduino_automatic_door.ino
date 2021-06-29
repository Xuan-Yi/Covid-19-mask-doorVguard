#include <SoftwareSerial.h>
#include <Servo.h>

//#define SETUP
//#define DEBUG

//buffer
#define buffer 9
//servo
Servo left_door;
#define left_door_pin 6
//bluetooth
SoftwareSerial BT(7, 8); // (RX, TX) of Arduino

enum BT_CMD
{
  OPENDOOR,
  CLOSEDOOR
};

static BT_CMD CMD = CLOSEDOOR;

void setup()
{
  //buffer
  pinMode(buffer, OUTPUT);
  pinMode(buffer, LOW);
  //servo
  left_door.attach(left_door_pin);
  //bluetooth
  BT.begin(9600);
#ifdef DEBUG
  Serial.begin(9600);
#endif
}

void loop()
{
  //setup program
#ifdef SETUP
  left_door.write(90);
#endif

  //main program
#ifndef SETUP
  if (BT.available())
  {
    char mes = 'o';
    mes = BT.read();
    if (mes == 'c') {
      CMD = CLOSEDOOR;
    }
    else
    {
      CMD = OPENDOOR;
    }
  }

#ifdef DEBUG
  Serial.print("CMD = ");
  if (CMD == OPENDOOR)
  {
    Serial.println("OPENDOOR");
  }
  else if (CMD == CLOSEDOOR)
  {
    Serial.println("CLOSEDOOR");
  }
#endif
  if (CMD == OPENDOOR)
  {
    left_door.write(88);
  }
  else if (CMD == CLOSEDOOR)
  {
    left_door.write(50);
    buzz(12000);
    delay(50);
  }
  else
  {
    left_door.write(88);
  }
#endif
}

void buzz(unsigned int freq)
{
  for (int t = 0; t <= 200; t++)
  {
    pinMode(buffer, HIGH);
    delayMicroseconds(1000000 / freq);
    pinMode(buffer, LOW);
    delayMicroseconds(1000000 / freq);
  }
}
