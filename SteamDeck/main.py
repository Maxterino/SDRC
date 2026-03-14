import sys

sd_input_joystick = 1 # Tijdelijke variable voor testing
DEADZONE = 3000


print("Hello World!")

#Functie voor deadzone elimineren op de SteamDeck joystick
def deadzone_eliminator(sd_input_joystick): 
    if sd_input_joystick <= 3000 and sd_input_joystick >= -3000:
        return 0
    else: 
        return sd_input_joystick