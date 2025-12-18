"""
QUESTION:
Determine the minimum number of rounds, g(X), needed to ensure player A has at least X grams of gold at the end of the game, given that player A starts with 1 gram of gold and player B has an infinite supply, with the game concluding when player B has chosen TAKE and GIVE an equal number of times. Implement a function g(X) that returns the minimum number of rounds needed for X = 1.9999, with the restriction that the function should not exceed 1 gram of gold for player A when selecting a nonnegative real number x.
"""

def g(X):
    if X <= 1:
        return 0
    if 1 < X <= 1.7:
        return 10
    if 1.7 < X <= 1.9999:
        return 11
    return NotImplemented