"""
QUESTION:
Write a function `is_composite(n)` to identify composite numbers. A composite number is a positive integer that has at least one positive divisor other than one or itself. Using this function, find all composite numbers in the range from 10 to 20, exclusive.
"""

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False