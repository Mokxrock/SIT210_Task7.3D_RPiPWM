import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

TRIG = 16 # Physical Pin 16 to GPIO 23 
ECHO = 18 # Physical Pin 18 to GPIO 24
LED = 12  # Physical Pin 13 to GPIO 18

GPIO.setup(TRIG,GPIO.OUT) # Set as Output
GPIO.setup(ECHO,GPIO.IN) # Set as Input
GPIO.setup(LED,GPIO.OUT) # Set as Output
 
GPIO.output(TRIG, False) # Turn Of Sensor 

p = GPIO.PWM(LED, 100) #LED as PWM output, with 100Hz frequency
p.start(0); # Starting from 0

try:
    while True:
        GPIO.output(TRIG, True) # Turn the Sensor On and Off between 0.00001 second 
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        #set the beggining of the time 
        while GPIO.input(ECHO)==0: 
            pulse_start = time.time()
        #set the Ending of the time 
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        
        distance = round(((pulse_duration * 34000) / 2 ), 2) # Calculation of distance by using the echo and sound 

        print ("distance:",distance,"cm") # Print Distance

        if distance<=50:  # Less then or Equal to 50cm
            for x in range(50,101,10): # Starting from 50 Hertz and End with 100hz and add 10hz to each loop 
                p.ChangeDutyCycle(x) # Change LED brightness
                time.sleep(0.1) # Stay for  0.1 Second
                
        elif distance>50: # More then 50cm
            for x in range(50,-1,-10): # Starting from 50hz it will decrease by 10hz at a time until then 0  
                p.ChangeDutyCycle(x) # Change LED brightness
                time.sleep(0.1) # Stay for  0.1 Second


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
