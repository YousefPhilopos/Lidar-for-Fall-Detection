#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);

  WiFi.mode(WIFI_STA);
  WiFi.begin("The Chill House", "WhatMustBeDone");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

  Serial.print("Subnet mask: ");
  Serial.println(WiFi.subnetMask());
}

void loop() {
  Serial.begin(115200);
  // nothing to do here
}