from machine import ADC, Pin, PWM
import time

sd_input_joystick = 1 # Tijdelijke variable voor testing
DEADZONE = 3000

# initialiseren van de motoren
left_pwm = PWM(Pin(11), freq=50) # B
right_pwm = PWM(Pin(17), freq=50) # A

right_dir = Pin(13, Pin.OUT)
left_dir = Pin(12, Pin.OUT)

# functies voor het besturen van de motoren
def stop():
    left_pwm.duty(0)
    right_pwm.duty(0)

def vooruit(snelheid):
    left_dir.value(0)
    right_dir.value(1)
    left_pwm.duty(snelheid)
    right_pwm.duty(snelheid)

def draai_links(sd_input_joystick):
    left_dir.value(0)
    right_dir.value(1)
    left_pwm.duty(sd_input_joystick * 1023)
    right_pwm.duty(0)

#Functie voor deadzone elimineren op de SteamDeck joystick
def deadzone_eliminator(sd_input_joystick): 
    if sd_input_joystick <= 3000 and sd_input_joystick >= -3000:
        return 0
    else: 
        return sd_input_joystick

while True:
    vooruit(200)