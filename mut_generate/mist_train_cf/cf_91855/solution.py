"""
QUESTION:
Create a function `digit_sum` that calculates the sum of all digits of a given integer in O(log n) time complexity, where n is the integer. The function should take an integer as input and return the sum of its digits.
"""

def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)