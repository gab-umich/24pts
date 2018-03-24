from fraction import Fraction
import math
import card
from enum import Enum

class Operation(Enum):
    VAL = 0
    A_ADD_B = 1
    A_MIN_B = 2
    B_MIN_A = 3
    A_MUL_B = 4
    A_DIV_B = 5
    B_DIV_A = 6


class Formula:
    """Require a, b to be Formula, optVal be int
        Find the result in the __init__"""
    def __init__(self, a, b, operation, optVal=None):
        self.A = a
        self.B = b
        self.Operation = operation
        self.Opt_Val = optVal
        self.result = None
        # TODO: how to find result depending on the operation??
        if operation == Operation.VAL:
            self.result = Fraction(optVal, 1)
        elif operation == Operation.A_ADD_B:
            self.result = a.result + b.result
        elif operation == Operation.A_MIN_B:
            self.result = a.result - b.result
        elif operation == Operation.B_MIN_A:
            self.result = b.result - a.result
        elif operation == Operation.A_MUL_B:
            self.result = a.result * b.result
        elif operation == Operation.A_DIV_B:
            self.result = a.result / b.result
        elif operation == Operation.B_DIV_A:
            self.result = b.result / a.result



def permutation(card1, card2, card3, card4, target=24):
    """Find the permutations with operator + - * and / using the 4 cards
    that matches the target, Default match value is 24"""
    r1 = card1.rank
    r2 = card2.rank
    r3 = card3.rank
    r4 = card4.rank

    f1 = Formula(0, 0, Operation.VAL, r1)
    f2 = Formula(0, 0, Operation.VAL, r2)
    f3 = Formula(0, 0, Operation.VAL, r3)
    f4 = Formula(0, 0, Operation.VAL, r4)

    
    print("----------------------------------")
    print("Beginning the permutation of number: {}, {}, {} and {}.".format(r1, r2, r3, r4))
    print("----------------------------------")

    # TODO: I am thinking about a class with 7 characteristics of permitted
    # Operations given two values. And then a set of 3 ``witnesses'' to keep track of the
    # Operation carried out so far.

    for op1 in Operation.__members__.items():
        inter_1 = Formula(f1, f2, op1)
        for op2 in Operation.__members__.items():
            inter_2 = Formula(inter_1, f3, op2)
            for op3 in Operation.__members__.items():
                inter_3 = Formula(inter_2, f4, op3)
                # arrived to final formula
                if inter_3 == 24:
                    print("Found 24!")
                    # TODO: replace this with a printer
