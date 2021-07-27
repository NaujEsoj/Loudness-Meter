import network, time, urequests
from machine import Pin, ADC
import utime

#TFT Screen libraries
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12)) #TFT PINS (Change numbers if necessary)
tft=TFT(spi,26,27,21) #TFT PINS (Change numbers if necessary)
tft.initr()
tft.rgb(True)

#variables
soundSensor = ADC(Pin(32)) #Pin where sensor device (Microphone) is connected
soundSensor.width(ADC.WIDTH_10BIT) #Allows to detect a better data lecture
soundSensor.atten(ADC.ATTN_11DB) #Gives a maximum input voltage of approximately 3.6v

#cleaning TFT screen
tft.fill(TFT.BLACK)

def main():

    #NetWork connection (WiFi)
    def connectWifi (name, password):
          global myNetwork
          myNetwork = network.WLAN(network.STA_IF)
          if not myNetwork.isconnected():              #If is not connected
              myNetwork.active(True)                   #activates the interface
              myNetwork.connect("name", "password")  #tryes to connect to network
              print('Connecting to network')
              timeout = time.time ()
              while not myNetwork.isconnected():           #If connection timed out
                  if (time.ticks_diff (time.time (), timeout) > 10):
                      return False
          return True



    #Uploading data to Thingspeak (https://thingspeak.com/)
    if connectWifi ("name", "password"):

        print ("Connection successful!")
        print('Network data (IP/netmask/gw/DNS):', myNetwork.ifconfig())
        tft.fill(TFT.BLACK)
        tft.text((30, 30), "WiFi:", TFT.GREEN, sysfont, 3)
        tft.text((20, 70), "ON", TFT.GREEN, sysfont, 8)
        utime.sleep(5)


        url = "https://api.thingspeak.com/update?api_key=**********" #URI created by Thingspeak API channel


        while True:
            #Transforming data to dB
            decibels = int((soundSensor.read() - 0) * (90 - 10) / (1023 - 0) + 10)
            print ("Loudness: {} dB".format(decibels))
            utime.sleep(30)

            #Connecting with API to Thingspeak
            answer = urequests.get(url+"&field1="+str(decibels))
            print(answer.text)
            print (answer.status_code)
            answer.close()

            #Show data on TFT screen
            tft.fill(TFT.BLACK)
            tft.text((0, 10), "Decibels", TFT.GREEN, sysfont, 3)
            tft.text((20, 60), str(decibels), TFT.RED, sysfont, 8) #Sending variable to TFT screen 


if __name__ == "__main__":
        main()