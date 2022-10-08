# LEGO type:standard slot:0 autostart

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
left_motor = Motor('E')
right_motor = Motor('F')
motion_sensor = MotionSensor()

def robot_move(left=10, right=10):
    left_motor.start(-left)
    right_motor.start(right)

def robot_stop():
    left_motor.stop()
    right_motor.stop()

def turn_left(angle=-90, speed=10):
    motion_sensor.reset_yaw_angle()
    # yaw is going to change from 0 to -90
    yaw = motion_sensor.get_yaw_angle()
    robot_move(left=-speed, right=speed)
    while yaw > angle:
        # print(yaw)
        yaw = motion_sensor.get_yaw_angle()       
    robot_stop()

def turn_right(angle=90, speed=10):
    motion_sensor.reset_yaw_angle()
    # yaw is going to change from 0 to 90
    yaw = motion_sensor.get_yaw_angle()
    robot_move(left=speed, right=-speed)
    while yaw < angle:
        # print(yaw)
        yaw = motion_sensor.get_yaw_angle()
    robot_stop()

while True:
    robot_move(left=20, right=20)
    wait_for_seconds(6)
    robot_stop()
    turn_right(speed=5)