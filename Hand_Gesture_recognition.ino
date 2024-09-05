#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F,16,2);
// 0x3F address i2c 
// 0x27 address i2c


void setup()
{
  Serial.begin(9600);

  lcd.init();

  lcd.backlight();
    lcd.setCursor(0,0);
   lcd.print("SIGN LANGUAGE        ");

  pinMode(13,OUTPUT);
}
void loop()
{
 int s1 = analogRead(A0);
  int s2 = analogRead(A1);
   int s3 = analogRead(A2);
    int s4 = analogRead(A3);
    
 Serial.println(s1);
 Serial.println("washroom");
 
 Serial.println(s2);
 Serial.println("drink water");
 Serial.println(s3);
 Serial.println("food");
 Serial.println(s4);
 Serial.println("fruit");
 //delay(3000);

if(s1 < 150)
{
  digitalWrite(13,LOW); 
   Serial.println("WashRoom         ");
   lcd.setCursor(0,1);
   lcd.print("   WASHROOM         ");
   delay(2000);
}

if(s2 < 200)
{
  digitalWrite(13 , HIGH); 
  Serial.println("Dring Water       ");
   lcd.setCursor(0,1);
   lcd.print("  DRINK WATER         ");
   delay(2000);
}

if(s3 < 150)
{
  digitalWrite(13,LOW); 
   Serial.println("Food         ");
   lcd.setCursor(0,1);
   lcd.print("      FOOD         ");
   delay(2000);
}

if(s4 < 130)
{
  digitalWrite(13 , HIGH); 
  Serial.println("Fruit      ");
   lcd.setCursor(0,1);
   lcd.print("      FRUIT         ");
  delay(2000);
}
else
{
    Serial.println("   NOTHING      ");
   lcd.setCursor(0,1);
   lcd.print("    NOTHING        ");

}
}