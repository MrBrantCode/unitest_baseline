"""
QUESTION:
Write a function named `sum_odd_integers` that calculates the sum of all odd integers between two given integers, `a` and `b` (inclusive), where `a` and `b` are not necessarily in order and `a` and `b` can be negative, zero, or positive.
"""

def sum_odd_integers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    total = 0
    
    if lower % 2 == 0:
        lower += 1
    
    for i in range(lower, upper + 1, 2):
        total += i
    
    return total