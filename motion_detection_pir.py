# motion_pir
from gpiozero import MotionSensor

pir = MotionSensor(4) #insert GPIO pin that the PIR sensor is connected to

while True:
    pir.wait_for_motion()
    print("motion detected")
    pir.wait_for_no_motion()
