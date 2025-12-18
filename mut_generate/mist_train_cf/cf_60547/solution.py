"""
QUESTION:
Write a function `find_trailing_zeros(n)` that calculates the number of trailing zeros in the factorial of a given integer `n`. The function should return the count of trailing zeros. Assume `n` is a non-negative integer.
"""

def find_trailing_zeros(n): 
    # Initialize result 
    count = 0
    i = 5
    while (n / i >= 1): 
        count += int(n / i) 
        i *= 5
  
    return int(count)