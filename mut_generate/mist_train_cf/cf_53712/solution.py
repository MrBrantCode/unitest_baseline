"""
QUESTION:
Write a function `digits(n)` that takes a non-negative integer `n` as input. Calculate the sum of the squares of even digits and the product of odd digits. If all digits are odd, return -1. Otherwise, return the sum of the squares of even digits minus the product of odd digits.
"""

def digits(n):
    sum_of_even_square = 0
    product_of_odd_digits = 1
    has_even_digits = False

    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            sum_of_even_square += digit * digit
            has_even_digits = True
        else:
            product_of_odd_digits *= digit
        n = n // 10

    if not has_even_digits:
        return -1
    else:
        return sum_of_even_square - product_of_odd_digits