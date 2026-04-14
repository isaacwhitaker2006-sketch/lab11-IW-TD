# https://github.com/isaacwhitaker2006-sketch/lab11-IW-TD/edit/main/test_calculator.py
#https://github.com/isaacwhitaker2006-sketch/lab11-IW-TD/edit/main/test_calculator.py
import unittest
from calculator import *

#Partner 1: Issac Whitaker
#Partner 2: Trent Diano

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 10), 12)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 2), 8)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -2), 0)


    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(0, 2), 0)
        self.assertEqual(mul(-2, 2), -4)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)
        self.assertEqual(div(0, 4), 0)
        self.assertEqual(div(-4, 2), -2)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(1, 5)
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        self.assertEqual(logarithm(10, 1), 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):     # expects ValueError
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
