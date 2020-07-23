#!/usr/bin/env python3

'''
Two methods used to test efficiency of the methods in fourth_project.py using time module.
The efficiency data is placed into a dictionary which makes the data easier to manipulate with key values etc.
For example, keys being used include the method names 'recursive_method' and 'math_method' and start/ending times.
'''

import time
import unittest
from fourth_project import FibonacciSequence

class TestEfficiency(unittest.TestCase):
    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = {}                          # dictionary to store efficiency test data

    def test_first_method(self):
        starting_time = time.time()                         # start timing for following code
        self._fibonacci_sequence.recursive_method(35)       # execution of code
        ending_time = time.time()                           # end timing for code above
        self._efficiency_data['recursive_method'] = ending_time - starting_time
        # _efficiency_data 'recursive_method' and timing sum added as keys to dictionary

    def test_second_method(self):
        starting_time = time.time()
        self._fibonacci_sequence.math_method(35)
        ending_time = time.time()
        self._efficiency_data['math_method'] = ending_time - starting_time

    def tearDown(self):
        print(self._efficiency_data)        # print all dictionary entries
        self._fibonacci_sequence = None     # clear test object
        self._efficiency_data.clear()       # delete data from the dictionary

if __name__ == '__main__':
    unittest.main()
