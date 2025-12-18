"""
QUESTION:
Create a function `digit_sum` that takes an integer `n` as input and returns the sum of all its digits. The function should handle negative integers and have a time complexity of O(log n), where n is the given integer. The implementation should not convert the integer to a string and should handle edge cases, such as when the integer is 0 or when it consists of only one digit.
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