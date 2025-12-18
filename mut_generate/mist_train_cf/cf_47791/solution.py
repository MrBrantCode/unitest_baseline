"""
QUESTION:
Write a function `largest_smallest_integers` that takes a list of integers as input and returns a tuple `(a, b, c, d)` where `a` is the largest negative even integer, `b` is the smallest non-negative even integer, `c` is the largest negative odd integer, and `d` is the smallest non-negative odd integer. If any of these categories are empty, the corresponding value in the tuple should be `None`.
"""

def largest_smallest_integers(lst):
    negative_evens = [x for x in lst if x < 0 and x % 2 == 0]
    non_negative_evens = [x for x in lst if x >= 0 and x % 2 == 0]
    negative_odds = [x for x in lst if x < 0 and x % 2 != 0]
    non_negative_odds = [x for x in lst if x >= 0 and x % 2 != 0]

    a = max(negative_evens) if negative_evens else None
    b = min(non_negative_evens) if non_negative_evens else None
    c = max(negative_odds) if negative_odds else None
    d = min(non_negative_odds) if non_negative_odds else None

    return (a, b, c, d)