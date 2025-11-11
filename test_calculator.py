# https://github.com/kmendicino/Lab10-KM-JP
# Partner 1: Kate Mendicino
# Partner 2: Jingjing Peng

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(3, 5), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(27, 3), 3)
        self.assertAlmostEqual(log(16, 2), 4)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)
        with self.assertRaises(ValueError):
            log(10, -2)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(-4, 2), -2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-10, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == "__main__":
    unittest.main()
