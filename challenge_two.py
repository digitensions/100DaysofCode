#!/usr/bin/env python3

"""
Coding Challenge #2, for use with test_challenge_two.py in tests/
"""

class Car:
    def __init__(self):
        self._speed = 0
        self._start_car = False

    def start_car(self):
        if self._start_car == False:
            self._start_car = True
        else:
            raise Exception("The car engine is already running.")

    def turn_off_car(self):
        if self._speed == 0:
            self._start_car = False
        else:
            raise Exception("You cannot turn off the car at speeds above 0.")

    def add_speed(self):
        self._speed += 5

    def remove_speed(self):
        if self._speed == 0:
            pass
        else:
            self._speed -= 5

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._start_car
