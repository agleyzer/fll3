from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
left_motor = Motor('E')
right_motor = Motor('F')
color_left = ColorSensor('A')
color_right = ColorSensor('B')

def robot_move(left=10, right=10):
    left_motor.start(-left)
    right_motor.start(right)

def robot_stop():
    left_motor.stop()
    right_motor.stop()

robot_move(5, 5)
while True:
    ll = color_left.get_reflected_light()
    rl = color_right.get_reflected_light()
    print(ll, rl)
    if ll < 60:
        print("go left!")
        robot_move(5, 10)
    elif rl < 60:
        print("go right!")
        robot_move(10, 5)
    else:
        print("go straight!")
        robot_move(5, 5)
    wait_for_seconds(0.5)
    