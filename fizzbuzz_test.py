import unittest
from fizzbuzz import *

class MyFirstTests(unittest.TestCase):

    def test_number(self):
        self.assertEqual(check_fizzbuzz(1), 1)
        self.assertEqual(check_fizzbuzz(34), 34)
        self.assertEqual(check_fizzbuzz(67), 67)

    def test_fizz(self):
        self.assertEqual(check_fizzbuzz(3), 'fizz')
        self.assertEqual(check_fizzbuzz(9), 'fizz')
        self.assertEqual(check_fizzbuzz(36), 'fizz')
        self.assertEqual(check_fizzbuzz(66), 'fizz')

    def test_buzz(self):
        self.assertEqual(check_fizzbuzz(5), 'buzz')
        self.assertEqual(check_fizzbuzz(50), 'buzz')
        self.assertEqual(check_fizzbuzz(65), 'buzz')
        self.assertEqual(check_fizzbuzz(10), 'buzz')

    def test_check_fizzbuzz(self):
        self.assertEqual(check_fizzbuzz(15), 'fizzbuzz')
        self.assertEqual(check_fizzbuzz(75), 'fizzbuzz')
        self.assertEqual(check_fizzbuzz(45), 'fizzbuzz')

    def test_fizzbuzz(self):
        set('1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, 10').issubset( fizzbuzz())
        set('14, fizzbuzz, 16').issubset( fizzbuzz())
        set('62, fizz, 64, buzz, fizz').issubset( fizzbuzz())
        set('89, fizzbuzz, 91, 92, fizz, 64, buzz, fizz').issubset( fizzbuzz())
