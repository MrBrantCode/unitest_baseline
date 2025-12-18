"""
QUESTION:
Create a function `sum_of_digit_squares` that takes a positive integer `num` less than or equal to 1000 and returns the sum of the squares of its digits without converting the integer to a string.
"""

def sum_of_digit_squares(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit**2
        num //= 10
    return sum