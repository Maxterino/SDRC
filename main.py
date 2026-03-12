from machine import ADC, Pin, PWM
import time

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

while True:
    vooruit(200)