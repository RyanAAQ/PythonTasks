from unittest import TestCase
from part2 import (add)

class ReturnSum(TestCase):

    def test_that_it_returns_the_sum(self):
    expected = 6
    actual = add("a1b2c3")
    self.assertEqual(actual, expected)
