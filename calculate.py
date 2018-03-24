import fraction
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
    def __init__(self, a, b, operation, optVal=None):
        self.A = a
        self.B = b
        self.Operation = operation
        self.Opt_Val = optVal




def permutation(card1, card2, card3, card4, target=24):
    """Find the permutations with operator + - * and / using the 4 cards
    that matches the target, Default match value is 24"""
    r1 = card1.rank
    r2 = card2.rank
    r3 = card3.rank
    r4 = card4.rank
    
    print("----------------------------------")
    print("Beginning the permutation of number: {}, {}, {} and {}.".format(r1, r2, r3, r4))
    print("----------------------------------")

# TODO: I am thinking about a class with 7 characteristics of permitted
# Operations given two values. And then a set of 3 ``witnesses'' to keep track of the
# Operation carried out so far.
