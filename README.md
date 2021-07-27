# Loudness-Meter
Detects loudness levels every 30 seconds (In decibels) using an ESP32, MAX9814, TFTscreen and micropython programation, also sends the information to Thinsgspeack using its API to be easily analyced.

For this project and in order for the TFT screen to work it was used the TFT micropython libraries from this other repositories:
- https://github.com/boochow/MicroPython-ST7735
- https://github.com/GuyCarver/MicroPython/blob/master/lib/ST7735.py

# Hardware

It requieres the following hardware:

- ESP32 (Wifi-Bluetooth)
- MAX9814 (other Microphones could work too, be shure to use the correct pins and libraries for the device used)


Optional (but recommended) hardware:

- TFT ST7735 Screen (Oled and other screen may work too, again, be shure to use the correct pins and libraries for the device used)
- HW-131 (5V – 3.3V) Power source

# Schematic Diagram

![Sensor de contaminacion acustica_bb](https://user-images.githubusercontent.com/55373104/127076405-7208acce-8d15-4d9e-82e4-75efaef4e826.png)

# Pins Table 
| Esp32 Pinout | Color | Connection |
| :---:         |     :---:      |          :---: |
| D12   | Brown     | (TFT) CS  |
| D13     | Blue       | (TFT) SDA      |
| D14   | Green     | (TFT) SCK   |
| D26    | Orange       | (TFT) RS      |
| D27   | Gray     | (TFT) RES   |
| D36     | Yellow       | (Max9814) Out      |


# Physical Components

Here is a image with all the devices mounted and configured:

![5555](https://user-images.githubusercontent.com/55373104/127080533-6c533adb-fd02-4731-8af4-5d63b625b5e2.jpg)

# Measurements

In this image we can see how Thingspeak shows the data received from the ESP32 and the MAx9814

![image](https://user-images.githubusercontent.com/55373104/127080868-880e56c2-f8ac-4cf7-a08c-acc201f30fda.png)



