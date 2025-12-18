"""
QUESTION:
Write a function `hasGroupsSizeX` that takes a list of integers `deck` as input, where `1 <= len(deck) < 10^4` and `0 <= deck[i] < 10^4`. The function should return `True` if the list can be divided into one or more groups of cards, where each group contains the same integer and has a size `X >= 2`. Otherwise, return `False`.
"""

from collections import Counter
import math

def hasGroupsSizeX(deck):
    count = Counter(deck)
    X = min(count.values())
    
    if X < 2:
        return False

    for i in count.values():
        if math.gcd(i, X) == 1:
            return False

    return True