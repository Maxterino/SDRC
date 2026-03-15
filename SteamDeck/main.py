import sys
import time
import struct
import socket
import pygame

#CONSTANTS
sd_input_joystick = 1 # Tijdelijke variable voor testing
DEADZONE = 3000
ESP32_IP = "192.168.1.2"
SLEEP_DURATION = 0.01
PORT = 42069


print("Hello World!")

#Functie voor deadzone elimineren op de SteamDeck joystick
def deadzone_eliminator(sd_input_joystick): 
    if sd_input_joystick <= 3000 and sd_input_joystick >= -3000:
        return 0
    else: 
        return sd_input_joystick