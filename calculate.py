import fraction
import math
import card

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

