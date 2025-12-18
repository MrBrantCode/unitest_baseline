"""
QUESTION:
Write a function `diff_square_sum_sum_square` that takes an integer `n` as input, where `1 <= n <= 10^5`, and returns the difference between the square of the sum of its digits and the sum of the squares of its digits.
"""

def diff_square_sum_sum_square(n):
    square_sum = 0
    sum_square = 0
    for digit in str(n):
        digit = int(digit)
        square_sum += digit
        sum_square += digit ** 2
    square_sum **= 2
    return square_sum - sum_square