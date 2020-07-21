import unittest
from challenge import counter

# Easy test cases, check that the count and sums work as advertised
class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEqual(counter('Jo'), 2)

    def test_easy_input_two(self):
        self.assertEqual(counter('Joanna'), 6)

# Medium tests check that the programme can handle spaces and non-alphabetic characters
class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter('Jo!@#$%^'), 2)

    def test_medium_input_two(self):
        self.assertEqual(counter('Joanna White'), 11)

# Hard tests check that exceptions and attribute errors are raised for empty or None entries
class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter(' '),0)

    def test_hard_input_two(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(counter(None),0)

if __name__ == '__main__':
    unittest.main()
