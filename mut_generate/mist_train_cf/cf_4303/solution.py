"""
QUESTION:
Create a function called `sum_of_squares` that takes two parameters, `num1` and `num2`, and returns the sum of their squares if the sum is a perfect square. If the sum is not a perfect square, or if either `num1` or `num2` is negative, the function should return -1. The function should not use any built-in functions or libraries to calculate the square root or check for perfect squares, and should have a time complexity of O(1) and a space complexity of O(1).
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