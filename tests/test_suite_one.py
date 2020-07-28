#!/usr/bin/env python3

import unittest
from tests.test_challenge_five import TestListChanger
from tests.test_wealth_manager import TestCalculate
from tests.test_challenge_four import TestEfficiency

def suite():
    suite = unittest.TestSuite()                                    # instantiate an object from suite method
    suite.addTest(TestListChanger('test_reverse_list'))             # import test method from TestListChanger from challenge five
    suite.addTest(TestListChanger('test_remove_first_and_last'))
    suite.addTest(TestListChanger('test_smallest_number'))

    suite.addTest(TestCalculate('test_calculate_medium_first'))     # additional tests from TestCalculate class, wealth manager
    suite.addTest(TestCalculate('test_calculate_medium_third'))

    suite.addTest(TestEfficiency('test_second_adding_method'))      # test from TestEfficiency class of challenge four
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()          # Going to create runner from TextTestRunner() of unittest
    runner.run(suite())                         # Run the suite with the runner
