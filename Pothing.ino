void setup() {
  Serial.begin(9600);

}

void loop() {
  int SensorValue = analogRead(A0);
  Serial.println(SensorValue);

}
