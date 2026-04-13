import unittest
from calculator import *

#Partner 1: Issac Whitaker
#Partner 2: Trent Diano

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,10), 12)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10,2), 8)
        self.assertEqual(subtract(0,5), -5)
        self.assertEqual(subtract(-2,-2), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0,5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2,8), 3)
        self.assertAlmostEqual(logarithm(10,100), 2)     
        self.assertAlmostEqual(logarithm(3,9), 2)

    def test_log_invalid_base(self):    
        with self.assertRaises(ValueError):
            logarithm(1,5)


    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()