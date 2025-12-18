"""
QUESTION:
Write a function `nth_root(n, y)` that calculates the nth root of a given integer y, where n ranges from 1 to 20 inclusive and y ranges from 1 to 1,000,000. The function should return the result with precision up to at least 10 decimal places.
"""

import math

def nth_root(n, y):
    if n < 1 or n > 20:
        return "N must be between 1 and 20 inclusive"
    if y < 1 or y > 1000000:
        return "Y must be between 1 and 1,000,000 inclusive"
    return round(math.pow(y, 1.0/n), 10)  # round to 10 decimal places