"""
QUESTION:
Implement a function `sum_of_squares(num1, num2)` that returns the sum of the squares of `num1` and `num2` if the sum is a perfect square; otherwise, return -1. The function should return -1 if either `num1` or `num2` is negative. The function must have a time complexity of O(1) and a space complexity of O(1), and it must not use any built-in functions or libraries to calculate the square root or check if a number is a perfect square.
"""

def sum_of_squares(num1, num2):
    if num1 < 0 or num2 < 0:
        return -1

    sum_squares = num1 ** 2 + num2 ** 2

    i = 0
    while i ** 2 <= sum_squares:
        if i ** 2 == sum_squares:
            return sum_squares
        i += 1

    return -1