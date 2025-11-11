# https://github.com/kmendicino/Lab10-KM-JP
# Partner 1: Kate Mendicino
# Partner 2: Jingjing Peng

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 4), -4)
        self.assertEqual(sub(-2, -3), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)
        with self.assertRaises(ValueError):
            log(2, -10)


    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(-10, 2), -5)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertEqual(math.hypot(5, 12), 13)
        self.assertAlmostEqual(math.hypot(1, 1), math.sqrt(2))

    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.sqrt(0), 0)
        with self.assertRaises(ValueError):
            math.sqrt(-4)

if __name__ == "__main__":
    unittest.main()
