"""
QUESTION:
Given a positive integer "n", write a function called "trailing_zeros" that takes in an integer "n" as a parameter and returns the number of trailing zeros in n!. Note that the function should not calculate the full factorial of "n" due to performance considerations. The input "n" is a positive integer greater than or equal to 5.
"""

def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count