import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

TRIG = 16 # GPIO 23
ECHO = 18 # GPIO 24
LED = 12 # GPIO 18
#i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(TRIG, False)

p = GPIO.PWM(LED, 50)
p.start(0);

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        
        distance = round(((pulse_duration * 34000) / 2 ), 2)

        #distance = round(distance+1.15, 2)
        print ("distance:",distance,"cm")

        if distance<=50:
            # GPIO.output(LED, GPIO.HIGH)
            # time.sleep(1)
            # GPIO.output(LED, GPIO.LOW)
            # time.sleep(1)
            for x in range(50,101,5):
                p.ChangeDutyCycle(x)
                time.sleep(0.1)
                
        elif distance>50:
            # GPIO.output(LED, GPIO.HIGH)
            # time.sleep(5)
            # GPIO.output(LED, GPIO.LOW)
            # time.sleep(5)
            for x in range(11,-1,-5):
                p.ChangeDutyCycle(x-0)
                time.sleep(0.1)


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
