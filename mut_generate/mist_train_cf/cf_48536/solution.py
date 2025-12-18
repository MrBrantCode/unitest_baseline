"""
QUESTION:
Create a function `find_trailing_zeroes(n)` that calculates the number of trailing zeroes in the factorial of a given non-negative integer `n`. The function should be efficient for large integers up to `n=1000`.
"""

def find_trailing_zeroes(n):
    count = 0
    i = 5
    while n//i >= 1:
        count += n//i
        i *= 5
    return count