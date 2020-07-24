#!/usr/bin/env python3

'''
First version of unittest for cinema.py
More script refactoring needed. Recursive errors from daisy chaining functions.
Uses unittest mock inport patch to allow inputs to questions to be provided (line 21)
'''

import sys
import unittest
from io import StringIO
from unittest.mock import patch
from cinema import choice
# from cinema import retry
# from cinema import ranking
# from cinema import exit_script

class TestFunctions(unittest.TestCase):

    def choiceTest(self, input, output):
        with patch('builtins.input', return_value=input), patch('sys.stdout', new=StringIO()) as fake_out:
            choice()
            self.assertEqual(fake_out.getvalue().strip(), output)

    def test_affirmed(self):
        self.choiceTest("joker", "The film Joker is in the top 50, positioned at number 39")

    def test_affirmed_two(self):
        self.choiceTest("US", "The film Us is in the top 50, positioned at number 9")

    def test_fail(self):
        self.choiceTest("carry on camping", "Your film choice doesn't appear in the list, what a shame")

    def test_fail_two(self):
        self.choiceTest("56o3w", "Your film choice doesn't appear in the list, what a shame")

if __name__ == '__main__':
    unittest.main()
