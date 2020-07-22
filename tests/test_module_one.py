#!/usr/bin/env python3

'''
Easy and Medium unit tests for simple averaging script
Imports unittest and function from tested module
Creates class and calls unittest.TestCase which comes with Python standard library 'Assertion' unit tests
An easy test would just check the sum works using correct inputs
A medium test checks for the function working when an incorrect input is entered (string, not int or float)
A test for module should always be named with prefix 'test_' and placed in folder called tests/
Do not have more than one test module per module.
'''

import unittest
from module_one import avg

class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1,2,3), 2)

    def test_easy_input_two(self):
        self.assertEqual(avg(10,10,10,10,10), 10)

class MediumTestCase(unittest.TestCase):

    def test_medium(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1,2,3,'Joanna'), 2)

    def test_medium_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1,2,3,'5'), 2)

if __name__ == '__main__':
    unittest.main()
