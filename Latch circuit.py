from gpiozero import LED
from gpiozero import Button
from gpiozero import Servo
from time import sleep

servo = Servo(18)
led = LED(6)
button = Button(5)

while True:
        button.wait_for_press()
        led.on()
        servo.min()
        sleep(0.4)
        button.wait_for_press()
        led.off()
        servo.max()
        sleep(0.4)