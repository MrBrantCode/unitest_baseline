"""
QUESTION:
Write a function `find_trailing_zeros(n)` that calculates the number of trailing zeros in the factorial of a given number `n`. The function should only count the number of trailing zeros and return this count as an integer.
"""

def find_trailing_zeros(n): 
    count = 0
    i = 5
    while n/i >= 1: 
        count += int(n/i) 
        i *= 5
    return int(count)