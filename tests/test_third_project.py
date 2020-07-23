#!/usr/bin/env python3

'''
Tests for checking console printed outputs.
Note the listening line of code, line 16, is essential for these tests.
'''

import sys
import unittest
from io import StringIO
from third_project import Profile

class TestPrintedOutput(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        # This is a listening line of code, waiting for printed output in console, when printed it's saved to 'stdout'
        self.profile = Profile("Joanna White", 44, "Digital Preservation Data Specialist", "British Film Institute")

    def test_name(self):
        self.profile.print_name()
        # Print out to console, which is saved into sys.stdout below.
        self.assertEqual(sys.stdout.getvalue().strip(), "Joanna White")
        # .strip() added to remove newline character added by profile.print_name() otherwise the test fails

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), '44')
        # Although the number is added without brackets above, it's still a string so needs testing this way

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), "Digital Preservation Data Specialist")

    def test_employer(self):
        self.profile.print_employer()
        self.assertEqual(sys.stdout.getvalue().strip(), "British Film Institute")

    def tearDown(self):
        self.profile = None
