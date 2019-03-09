import unittest
from fizzbuzz import *

class MyFirstTests(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(check_fizzbuzz(1), 1)
  
