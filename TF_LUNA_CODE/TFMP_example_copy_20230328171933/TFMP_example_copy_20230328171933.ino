#include <HardwareSerial.h>

// Define the serial port to use
#define TFMINI_SERIAL_PORT Serial2

void setup() {
  Serial.begin(9600); // Initialize serial communication for debugging
  TFMINI_SERIAL_PORT.begin(115200); // Initialize serial communication for the TFmini Plus LiDAR
}

void loop() {
  // Check if there is any data available on the TFmini Plus LiDAR serial port
  if (TFMINI_SERIAL_PORT.available() >= 9) {
    // Read the data packet from the TFmini Plus LiDAR
    uint8_t buffer[9];
    TFMINI_SERIAL_PORT.readBytes(buffer, 9);

    // Check if the data packet starts with the correct header bytes
    if (buffer[0] == 0x59 && buffer[1] == 0x59) {
      // Extract the distance value from the data packet
      uint16_t distance = (buffer[3] << 8) | buffer[2];

      // Print the distance value to the serial monitor
      Serial.print("Distance: ");
      Serial.println(distance);
    }
  }
}





