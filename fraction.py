from math import gcd

# START OF CLASS DEFINITION
# EVERYTHING IS PUBLIC
class Fraction:
    """A simple class that supports integers and four operations."""
    numerator = 1
    denominator = 1

    # Do not modify the __init__ function at all!
    def __init__(self, nu, de):
        """Assign numerator and denominator, then simplify"""
        self.numerator = nu
        self.denominator = de
        self.simplify()


    # Do not modify the simplify function at all!
    def simplify(self):
        """_________Require: self.numerator is an int,
                             self.denominator is an int,
                    Modify:  Simplify numerator and denominator,
                    Effect:  GCD(numerator, denominator) == 1"""
        try:
            if self.denominator == 0:
                raise ValueError("denominator is zero ")
            gcd_ = gcd(self.numerator, self.denominator)
            self.numerator /= gcd_
            self.denominator /= gcd_

        except ValueError as err:
            print(err)

    # Do not modify the print function at all!
    def print(self):
        print("{}/{}".format(self.numerator, self.denominator))
# END OF CLASS DEFINITION


def add(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 added by frac2 and simplified"""

def sub(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac2 subtracted from frac1 and simplified"""

def mul(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 multiplied by frac2 and simplified"""

def div(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 divided by frac2 simplified"""
    # this is tricky! What can go wrong in div??
