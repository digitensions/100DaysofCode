#!/usr/bin/env python3

'''
Tests for classes, using setUp and tearDown
Instantiating objects to access the class
'''

import unittest
from second_project import Counter

class EasyTestCase(unittest.TestCase):
    # Set up your objects here so you don't have to repeat in following tests (test_easy_input)
    def setUp(self):
        self.counter = Counter()

    # Checks if the value begins at zero
    def test_easy_input(self):
        self.assertEqual(self.counter.get_value(), 0)

    # Checks if clear() returns value to 0
    def test_easy_input_two(self):
        self.counter.clear()
        self.assertEqual(self.counter.get_value(), 0)

    # tearDown is used to clear out the object. Good practise to set to None. Add information to trash.
    def tearDown(self):
        self.counter = None

class MediumTestCase(unittest.TestCase):
    # Set up your objects here so you don't have to repeat in following tests (test_easy_input)
    def setUp(self):
        self.counter = Counter()

    # Checks if the add and remove method increment/remove variable values
    def test_med_input(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 2)

    # Checks if add method incrementally increases variable value
    def test_med_input_two(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.assertEqual(self.counter.get_value(), 3)

    # tearDown is used to clear out the object. Good practise to set to None. Add information to trash.
    def tearDown(self):
        self.counter = None

class HardTestCase(unittest.TestCase):
    # Set up your objects here so you don't have to repeat in following tests (test_easy_input)
    def setUp(self):
        self.counter = Counter()

    # Checks if the lowest value received is 0 (not minus numbers)
    def test_hard_input(self):
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 0)

    # Checks if add method incrementally increases variable value
    def test_hard_input_two(self):
        for _ in range(0, 1000):
            self.counter.add()
        for _ in range(0, 500):
            self.counter.remove()
        self.assertEqual(self.counter.get_value(),500)

    # tearDown is used to clear out the object. Good practise to set to None. Add information to trash.
    def tearDown(self):
        self.counter = None

if __name__ == '__main__':
    unittest.main()
