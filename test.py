import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


class FractionTestCase(unittest.TestCase):
    def test_ctor(self):
        frac1 = Fraction(1, 2)  # 1/2
        self.assertEqual(frac1.numerator, 1)
        self.assertEqual(frac1.denominator, 2)
        frac2 = Fraction(5, 3)  # 5/3
        self.assertEqual(frac2.numerator, 5)
        self.assertEqual(frac2.denominator, 3)
        frac3 = Fraction(4, 2)  # 2
        self.assertEqual(frac3.val(), 2, "simplify method")
        frac4 = Fraction(12, 1)  # 12
        self.assertEqual(frac4.val(), 12, "int handling method")
        frac5 = Fraction(0, 3)  # 0
        self.assertEqual(frac5.val(), 0, "0 handling method")
        frac6 = Fraction(12, 8)  # 3/2
        self.assertEqual(frac6.numerator, Fraction(3, 2).numerator, "simplify method")
        self.assertEqual(frac6.denominator, Fraction(3, 2).denominator, "simplify method")

    def test_add(self):

    # TODO: compete this

    def test_sub(self):

    # TODO: compete this

    def test_div(self):

    # TODO: compete this

    def test_mul(self):
# TODO: compete this


if __name__ == '__main__':
    unittest.main()
