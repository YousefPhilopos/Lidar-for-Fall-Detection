#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino.h>
#include <Wire.h>        // Instantiate the Wire library
#include <TFLI2C.h>      // TFLuna-I2C Library v.0.1.1

TFLI2C tflI2C;

const char* ssid = "LabLocal"; //LabLocal
const char* password = "AssissLocoLab"; //AssissLocoLab



int16_t  tfDist;    // distance in centimeters
int16_t  tfAddr = TFL_DEF_ADR;  // Use this default I2C address

void setup() {
  Serial.begin(115200);
  Wire.begin(); 


  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {





  if(tflI2C.getData(tfDist, tfAddr)){
    }


  
  HTTPClient http;
  String url = "http://192.168.4.36:8000/new";
  String data = "task=" + (String(tfDist)+" cm / " + String(tfDist/2.54)+" inches");
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

  delay(5); // Submit data every 0.05 seconds


}