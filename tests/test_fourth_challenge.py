#!/usr/bin/env python3

import time
import unittest
from fourth_challenge import EfficiencyAdding

class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = {}

    def test_first_adding_method(self):
        start_time = time.time()
        self._efficiency.adding_two_first_method(5)
        end_time = time.time()
        self._efficiency_data['adding_two_first_method'] = end_time - start_time

    def test_second_adding_method(self):
        start_time = time.time()
        self._efficiency.adding_two_second_method(5)
        end_time = time.time()
        self._efficiency_data['adding_two_second_method'] = end_time - start_time


    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None

if __name__ == '__main__':
    unittest.main()