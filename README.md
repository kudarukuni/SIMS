# SIMS
<h1>The Smart Inventory Management System</h1> <br>
SIMS was designed for Smart Manufacturing purposes. The solution will allow for fast smart inventory stock taking by using the ESP32Cam and ESP8266 IoT modules.

<b>Arduino IDE Dependencies</b> <br>
Install Boards Manager > ESP32CAM via https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json <br>
Install Boards Manager > ESP8266 via https://arduino.esp8266.com/stable/package_esp8266com_index.json <br>
Download and add ESP32QRCodeReader library via Sketch > Include Library > Add .zip <br>
Install SoftwareSerial library via Sketch > Include Library > Manage Libraries <br>

<b>Python IDLE Dependencies</b> <br>
pip install serial <br>
pip install pymysql <br>

<b>XAMPP Design</b> <br>
Create database sims_db & import sims_db.sql <br>

<b>Hardware Design</b> <br>
Connect ESP8266 TX, RX pins to ESP32CAM UOR, UOT Pins <br>
