#!/usr/bin/env python3

import unittest
from challenge import Car

'''
This easy test of class Car must setUp an instance self.car = Car() and start the engine with self.car.start_car().
Add speed and check speed using assertEqual, stop car and check speed is 0, and is not -10.
Stop car, turn off and set instance to None.
'''

class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 20)

    def test_easy_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)
        self.assertIsNot(self.car.current_speed(), -10)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None

'''
This medium test of class Car must setUp an instance self.car = Car() and start the engine with self.car.start_car().
Check to see if a car can be started twice, raise an exception on challenge.py and check in test.
Check to see if a car engine can be turned off at 20mph. Raise exception in challenge.py and check in test.
Stop car, turn off and set instance to None.
'''

class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        with self.assertRaises(Exception):
            self.car.start_car()

    def test_medium_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        with self.assertRaises(Exception):
            self.car.turn_off_car()

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None

'''
This hard test of class Car must setUp an instance self.car = Car() and start the engine with self.car.start_car().
Check to see if removing more speed than is added results in a - figure. If/else established in challenge.py to prevent this.
Check to see if a car can be stopped twice and have speed other than 0.
Stop car, turn off and set instance to None.
'''

class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 0)

    def test_hard_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()
