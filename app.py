from flask import Flask
import RPi.GPIO as GPIO


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

stop = 0
DutyCycleA = 55
DutyCycleB  = 35
freq = 50
pinTrigger = 17
pinEcho = 18

rb = 9
rf = 10
lf = 7
lb = 8
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(rb, GPIO.OUT)
GPIO.setup(rf, GPIO.OUT)
GPIO.setup(lb, GPIO.OUT)
GPIO.setup(lf, GPIO.OUT)
print('Ultra measurement')

#Set Gpio to user PWM software
pwmLf =  GPIO.PWM(lf, freq)
pwmLb = GPIO.PWM(lb, freq)
pwmRb = GPIO.PWM(rb, freq)
pwmRf = GPIO.PWM(rf, freq)

#start PWM software with 0 duty cycle
pwmLf.start(stop)
pwmRf.start(stop)


def moveForwards():
	pwmLf.ChangeDutyCycle(DutyCycleB)
	pwmRf.ChangeDutyCycle(DutyCycleA)
	pwmLb.ChangeDutyCycle(stop)
	pwmRb.ChangeDutyCycle(stop)

def stopMotors():
	pwmLf.ChangeDutyCycle(stop)
	pwmRf.ChangeDutyCycle(stop)
	pwmLb.ChangeDutyCycle(stop)
	pwmRb.ChangeDutyCycle(stop)
def Right():
        pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
        pwmMotorABackwards.ChangeDutyCycle(Stop)
        pwmMotorBForwards.ChangeDutyCycle(Stop)
        pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
app = Flask(__name__)

@app.route('/')
def index():
      moveForwards()
      return 'Moving'

@app.route('/stop')
def stopEngine():
      stopMotors()
      return "<h1 style'color: red'>Stopping ...... </h1>"
@app.route('/r')
def moveRight():
     Right()
     return 'Moving to the right'


app.run()
