#include <WiFi.h>
#include <HTTPClient.h>
const char* ssid = "The Chill House";
const char* password = "WhatMustBeDone";
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  HTTPClient http;
  String url = "http://192.168.4.36:8000/new"; // Replace with the URL of your form's action URL
  String data = "Ultrasonic=Ultrasonic&50.0m=50.0m"; // Replace with the field names and values you want to submit
  http.begin(url);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  int httpCode = http.POST(data);
  if (httpCode > 0) {
    String response = http.getString();
    Serial.println("Server response: " + response);
  } else {
    Serial.println("Error submitting form: " + http.errorToString(httpCode));
  }
  http.end();
}
void loop() {
  // Nothing to do in the loop
}