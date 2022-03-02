from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO
import serial
import time

app = Flask(__name__)

py_serial = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
)

@app.route("/")

@app.route("/led/r")
def led_r():
    try:
        commend='r'
        py_serial.write(commend.encode())
        time.sleep(0.1)
        return "ok"
    except expression as identifier:
        return "fail"


@app.route("/led/y")
def led_y():
    try:
        commend='y'
        py_serial.write(commend.encode())
    except expression as identifier:
        return "fail"

@app.route("/led/g")
def led_g():
    try:
        commend='g'
        py_serial.write(commend.encode())
    except expression as identifier:
        return "fail"

if __name__ == "__main__":
        app.run(debug=True,port=80,host="0.0.0.0")
