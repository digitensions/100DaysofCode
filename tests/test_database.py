#!/usr/bin/env python3

import sys
import unittest
from io import StringIO
from unittest.mock import patch

from database import main


class MyTestCase(unittest.TestCase):

    def TestWord(self, word, response):
        with patch('builtins.input', return_value=word), patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue().strip(), response)

    def test_confirm_easy(self):
        self.TestWord("supernova", "The word you have chosen 'supernova' has the following definitions: Spectacular explosion of a star at the end of its lifetime")
    def test_confirm_med(self):
        self.TestWord("titanic", "Sorry, your word is not found")
    def test_confirm_hard(self):
        self.TestWord("t1t4n1c", "Sorry, your word is not found")
    def test_confirm_hard_two(self):
        self.TestWord(False, "The word you have chosen 'False' has the following definitions: Not in keeping with the reality or the facts.")

if __name__ == '__main__':
    unittest.main()
