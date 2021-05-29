#include <SoftwareSerial.h>
#include <Servo.h>

//#define SETUP
//#define DEBUG

//buffer
#define buffer 9
//servo
Servo left_door, right_door;
#define left_door_pin 6
#define right_door_pin 5
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
  right_door.attach(right_door_pin);
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
  right_door.write(90);
#endif

  //main program
#ifndef SETUP
  if (BT.available())
  {
    char mes = 'n';
    mes = BT.read();
    switch (mes)
    {
    case 'o':
      CMD = OPENDOOR;
      break;
    case 'c':
      CMD = CLOSEDOOR;
      break;
    default:
      CMD = CLOSEDOOR;
    }
  }

#ifdef DEBUG
  Serial.print("CMD = ");
  switch (CMD)
  {
  case OPENDOOR:
    Serial.println("OPENDOOR");
    break;
  case CLOSEDOOR:
    Serial.println("CLOSEDOOR");
    break;
  }
#endif
  switch (CMD)
  {
  case OPENDOOR:
    left_door.write(0);
    right_door.write(180);
    break;
  case CLOSEDOOR:
    left_door.write(90);
    right_door.write(90);
    buzz(12000);
    delay(50);
    break;
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
