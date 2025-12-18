"""
QUESTION:
Write a function `compute_sum` that takes a positive integer as input and returns the sum of its digits. The input number can be any positive integer, but if a non-positive integer is provided, the function should return 0. The function should be recursive.
"""

def compute_sum(number):
    if number < 1:
        return 0
    elif number < 10:
        return number
    else:
        last_digit = number % 10
        return last_digit + compute_sum(number // 10)