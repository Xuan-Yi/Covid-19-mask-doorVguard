#include <SoftwareSerial.h>
#include <Servo.h>

//#define SETUP
//#define DEBUG

//buffer
#define buffer 9
//servo
Servo left_door;
#define left_door_pin 65
//bluetooth
SoftwareSerial BT(7, 8); // (RX, TX) of Arduino

enum BT_CMD
{
  NOTHING,
  OPENDOOR,
  CLOSEDOOR
};

static BT_CMD CMD = NOTHING;

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
    char mes = 'n';
    mes = BT.read();
    if (mes == 'o')
    {
      CMD = OPENDOOR;
    }
    else if (mes == 'c')
    {
      CMD = CLOSEDOOR;
    }
    else
    {
      CMD = NOTHING;
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
  else
  {
    Serial.println("NOTHING");
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
