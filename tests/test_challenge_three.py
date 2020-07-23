#!/usr/bin/env python3

'''
Third challenge, testing console printed outputs.
Listening line required using StringIO and sys.stdout.
'''

import sys
import unittest
from io import StringIO
from third_challenge import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        # Todo: use the object printer to add a name to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is the same as the inputted name.
        self.printer.set_value("Joanna White")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Joanna White")

    def test_value_job(self):
        # Todo: use the object printer to add a job to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is the same as the job.
        self.printer.set_value("Digital Preservation Data Specialist")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Digital Preservation Data Specialist")

    def tearDown(self):
        # Todo: set the printer object to None.
        self.printer = None

if __name__ == '__main__':
    unittest.main()
