import unittest
from fizzbuzz import *

class MyFirstTests(unittest.TestCase):

    def test_number(self):
        self.assertEqual(check_fizzbuzz(1), 1)

    def test_fizz(self):
        self.assertEqual(check_fizzbuzz(3), 'fizz')

    def test_buzz(self):
        self.assertEqual(check_fizzbuzz(5), 'buzz')
