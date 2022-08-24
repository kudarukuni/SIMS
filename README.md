# SIMS
The Smart Inventory Management  System was designed for Smart Manufacturing purposes. The solution will allow for fast smart inventory stock taking by using the ESP32Cam and ESP8266 IoT modules.

Arduino IDE Dependencies
Install Boards Manager > ESP32CAM via https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
Install Boards Manager > ESP8266 via https://arduino.esp8266.com/stable/package_esp8266com_index.json
Download and add ESP32QRCodeReader library via Sketch > Include Library > Add .zip
Install SoftwareSerial library via Sketch > Include Library > Manage Libraries

Python IDLE Dependencies
pip install serial
pip install pymysql

XAMPP Design
Create database sims_db & import sims_db.sql

Hardware Design
Connect ESP8266 TX, RX pins to ESP32CAM UOR, UOT Pins
