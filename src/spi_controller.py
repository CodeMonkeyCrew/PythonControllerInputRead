import spidev
import time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0)
spi.bits_per_word = 8
#spi.cshigh = False
spi.max_speed_hz = 9600
#spi.mode = 0b00 # clock polarity 0, clock phase 0
spi.threewire = False
#send data to server over spi and recieve the gamestat
#the gamestate is forwerded to the connected clients
currentstate = []



def send_receive_over_spi(player, message):
    try:
        print("send:", message)
        resp = spi.xfer([(message[0] & 0xFF),message[1] & 0XFF])
        print("received: ", resp)
        if currentstate != resp:
            currentstate = resp
            player.connection.send(currentstate)      
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 

