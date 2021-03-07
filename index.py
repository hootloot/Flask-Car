import RPi.GPIO as GPIO
from time import sleep

from flask import Flask, render_template, request
app = Flask(__name__)

#pins
A = 17
B = 22
C = 23
D = 24

#setup

def init():
    print('setup')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(B,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)

#shorterfunctions

def sforward(sec):
    GPIO.cleanup()
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)

def sreverse(sec):
    GPIO.cleanup()
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, True)

def sleft(sec):
    GPIO.cleanup()
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)

def sright(sec):
    GPIO.cleanup()
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, True)

#simple function

def stop():
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.cleanup()

def forward():
    GPIO.cleanup()
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)

def reverse():
    GPIO.cleanup()
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, True)

def left():
    GPIO.cleanup()
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)

def right():
    GPIO.cleanup()
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, True)



@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('forward') == 'forward':
            forward()
            print('forward')
        elif  request.form.get('reverse') == 'reverse':
            reverse()
            print("reverse")
        elif request.form.get('left') == 'left':
            left()
            print('left')
        elif request.form.get('right') == 'right':
            right()
            print('right')  
        elif request.form.get('stop') == 'stop':
            stop()
            print('stop')
        #shorter commands
        elif  request.form.get('sreverse') == 'sreverse':
            sreverse(1)
            print("sreverse")
        elif request.form.get('sleft') == 'sleft':
            sleft(1)
            print('sleft')
        elif request.form.get('sright') == 'sright':
            sright(1)
            print('sright')  
        elif request.form.get('sforward') == 'sforward':
            sforward(1)
        else:
            return render_template("style.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("style.html")


if __name__ == '__main__':
    init()
    app.run()
