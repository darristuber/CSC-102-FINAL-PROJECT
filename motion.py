from gpiozero import MotionSensor

pir = MotionSensor(4)

i = 0
while True:
    pir.wait_for_motion()
    print("Motion detected", i)
    pir.wait_for_no_motion()
    print("Wait", i)
    i += 1