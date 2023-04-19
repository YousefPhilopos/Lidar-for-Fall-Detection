#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "The Chill House";
const char* password = "WhatMustBeDone";
const char* serverAddress = "10.0.0.212";
int serverPort = 8000;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

  Serial.print("Pinging server ");
  Serial.print(serverAddress);
  Serial.print(":");
  Serial.print(serverPort);
  Serial.print("...");

  WiFiClient client;
  if (client.connect(serverAddress, serverPort)) {
    Serial.println("success!");
  } else {
    Serial.println("failed!");
  }

  client.stop();
}

void loop() {
  // Nothing to do in the loop for this example
}