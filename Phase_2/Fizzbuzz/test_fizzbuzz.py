import unittest

from fizzbuzz import generate 
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
  def test_lists_values_up_to_one(self):
    self.assertEqual(generate(1), "1")

  def test_prints_Fizz(self):
    for i in [3, 6, 9, 18]:
      print('testing', i)
      assert fizzbuzz(i) == 'Fizz'

  def test_prints_Buzz(self):
    for i in [5, 10, 20, 25]:
      print('testing', i)
      assert fizzbuzz(i) == 'Buzz'

  def test_prints_Fizzbuzz(self):
    for i in [15, 30, 45, 60, 75, 90]:
      print('testing', i)
      assert fizzbuzz(i) == 'FizzBuzz'
    