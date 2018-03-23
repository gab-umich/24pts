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
        self.numerator = int(nu)
        self.denominator = int(de)
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
            self.numerator //= gcd_
            self.denominator //= gcd_

        except ValueError as err:
            print(err)

    # Do not modify the print function at all!
    def print(self):
        print("{}/{}".format(self.numerator, self.denominator))

    def __add__(self, frac_to_add):
        return add(self, frac_to_add)

    def __mul__(self, frac_to_mul):
        return mul(self, frac_to_mul)

    def __sub__(self, frac_to_sub):
        return sub(self, frac_to_sub)

    def __truediv__(self, frac_to_div):
        return div(self, frac_to_div)


# END OF CLASS DEFINITION


def add(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 added by frac2 and simplified"""
    new_nu = frac1.numerator * frac2.denominator + frac2.numerator * frac1.denominator
    new_de = frac1.denominator * frac2.denominator
    new_frac = Fraction(new_nu, new_de)
    return new_frac

def sub(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac2 subtracted from frac1 and simplified"""
    new_nu = frac1.numerator * frac2.denominator - frac2.numerator * frac1.denominator
    new_de = frac1.denominator * frac2.denominator
    new_frac = Fraction(new_nu, new_de)
    return new_frac

def mul(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 multiplied by frac2 and simplified"""
    new_frac = Fraction(frac1.numerator * frac2.numerator, frac1.denominator * frac2.denominator)
    return new_frac


def div(frac1, frac2):
    """________Require: frac1 and frac2 are simplified
               Modify:  nothing
               Effect:  return frac1 divided by frac2 simplified"""
    # this is tricky! What can go wrong in div??
    new_nu = frac1.numerator * frac2.denominator
    new_de = frac1.denominator * frac2.numerator
    new_frac = Fraction(new_nu, new_de)
    return new_frac