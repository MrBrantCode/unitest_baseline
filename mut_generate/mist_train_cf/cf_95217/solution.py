"""
QUESTION:
Create a function `digit_sum(n)` that calculates the sum of all digits of an integer `n` in O(log n) time complexity, handling both positive and negative integers without converting the integer to a string. The function should also handle edge cases where `n` is 0 or consists of only one digit.
"""

def digit_sum(n):
    if n == 0:
        return 0
    if n < 0:
        n = abs(n)
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    return sum_of_digits