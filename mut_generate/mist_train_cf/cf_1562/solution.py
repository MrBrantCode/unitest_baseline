"""
QUESTION:
Design a function named `find_maximum` that takes three integer inputs `a`, `b`, and `c`. The function should return the maximum of the three inputs without using any comparison operators (e.g., >, <, >=, <=) or mathematical functions (e.g., max(), min()).
"""

def find_maximum(a, b, c):
    diff1 = a - b  # difference between a and b
    diff2 = a - c  # difference between a and c

    mask1 = (diff1 >> 31) & 1  # mask to check if diff1 is negative
    mask2 = (diff2 >> 31) & 1  # mask to check if diff2 is negative

    sign_diff = mask1 ^ mask2  # sign difference between diff1 and diff2

    # If sign_diff is 0, then diff1 and diff2 have the same sign
    # If sign_diff is 1, then diff1 and diff2 have different signs
    # If sign_diff is 0, we return a (as it is greater or equal to b and c)
    # If sign_diff is 1, we return the maximum of b and c (since a is smaller)

    return a * (1 - mask1 * mask2) + b * mask1 * (1 - mask2) + c * mask1 * mask2