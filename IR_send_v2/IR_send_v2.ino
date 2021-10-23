#include <IRremote.h>

IRsend irsend;

String inByte;

char str[10];
char *ptr;
long ret;


void establishContact();


void setup()
{
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  establishContact();
}

void loop() {
  if (Serial.available() > 0){
    while (Serial.available() > 0) {
      inByte = Serial.readString();
    }

    str[0] = inByte[0];
    str[1] = inByte[1];
    str[2] = inByte[2];
    str[3] = inByte[3];
    str[4] = inByte[4];
    str[5] = inByte[5];
    str[6] = inByte[6];
    str[7] = inByte[7];
    str[8] = inByte[8];
    str[9] = inByte[9];

    ret = strtoul(str, &ptr, 16);
    Serial.println(ptr);
    Serial.println(str);
    Serial.println(ret);
    
    
    if (inByte) {
      Serial.println("success");
      for (int i = 0; i < 1; i++) {
          irsend.sendNEC(ret, 32);
          //Serial.println(inByte);
          inByte = "";
          delay(250);
      }
    }
  }
 
  //delay(5000); //5 second delay between each signal burst
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('.');   // send a "."
    delay(300);
  }
}
