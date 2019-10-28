from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
from time import sleep

Motor1A = 5  #DIR1
Motor1B = 12  #BRK1
Motor1E = 6  #PWM1
Motor2A = 13  #DIR2
Motor2B = 26  #BRK2
Motor2E = 16  #PWM2

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)

def stop1():
    print "stop"
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)

def forward():
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    print "Forward"

def back():
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
def left():
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    print "left"
def right():
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    print "right"

app = Flask(__name__)

print "DOne"

a=1
@app.route("/")

def index():
    return render_template('robot.html')
    print "back"


@app.route('/left_side')
def left_side():
    data1="LEFT"
    print "Left"
    left()
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   print "Right"
   right()
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   print "Forward"
   forward()
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   print "Back"
   back()
   return 'true'
@app.route('/stop')
def stop():
   data1="STOP"
   print "Stop"
   stop1()
   return  'true'

if __name__ == "__main__":
 setup()
print "Start"
 app.run(host='0.0.0.0',port=5010)

