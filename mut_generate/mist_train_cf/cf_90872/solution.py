"""
QUESTION:
Create a function named `sum_of_digits` that takes a positive integer as input and returns the sum of its digits excluding any digits that are divisible by 3.
"""

def sum_of_digits(num):
    num_str = str(num)
    sum = 0

    for digit in num_str:
        digit_int = int(digit)
        if digit_int % 3 != 0:
            sum += digit_int

    return sum