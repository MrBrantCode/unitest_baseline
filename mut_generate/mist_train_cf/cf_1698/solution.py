"""
QUESTION:
Given a positive integer "n" where n is less than or equal to 10^6, write a function called "trailing_zeros" that takes in "n" as a parameter and returns the number of trailing zeros in n!, the factorial of "n".
"""

def trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count