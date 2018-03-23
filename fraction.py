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
        if self.numerator == 0:
            print("0")
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


def add(arg1, arg2):
    """________Require: arg1 and arg2 are simplified
                        arg1, arg2 can be a Fraction class or an integer
               Modify:  nothing
               Effect:  return frac1 added by frac2 and simplified"""
    if isinstance(arg1, int):
        arg1 = Fraction(arg1, 1)
    if isinstance(arg2, int):
        arg2 = Fraction(arg2, 1)
    new_nu = arg1.numerator * arg2.denominator + arg2.numerator * arg1.denominator
    new_de = arg1.denominator * arg2.denominator
    new_val = Fraction(new_nu, new_de)
    return new_val

def sub(arg1, arg2):
    """________Require: arg1 and arg2 are simplified
               Modify:  nothing
               Effect:  return arg2 subtracted from arg1 and simplified"""
    if isinstance(arg1, int):
        arg1 = Fraction(arg1, 1)
    if isinstance(arg2, int):
        arg2 = Fraction(arg2, 1)
    new_nu = arg1.numerator * arg2.denominator - arg2.numerator * arg1.denominator
    new_de = arg1.denominator * arg2.denominator
    new_val = Fraction(new_nu, new_de)
    return new_val

def mul(arg1, arg2):
    """________Require: arg1 and arg2 are simplified
               Modify:  nothing
               Effect:  return arg1 multiplied by arg2 and simplified"""
    if isinstance(arg1, int):
        arg1 = Fraction(arg1, 1)
    if isinstance(arg2, int):
        arg2 = Fraction(arg2, 1)
    new_val = Fraction(arg1.numerator * arg2.numerator, arg1.denominator * arg2.denominator)
    return new_val


def div(arg1, arg2):
    """________Require: arg1 and arg2 are simplified
               Modify:  nothing
               Effect:  return arg1 divided by arg2 simplified"""
    # this is tricky! What can go wrong in div??
    if isinstance(arg1, int):
        arg1 = Fraction(arg1, 1)
    if isinstance(arg2, int):
        arg2 = Fraction(arg2, 1)
    new_nu = arg1.numerator * arg2.denominator
    new_de = arg1.denominator * arg2.numerator
    new_val = Fraction(new_nu, new_de)
    return new_val
