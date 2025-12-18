"""
QUESTION:
Create a function called `is_armstrong_number` that takes an integer as input and returns `True` if the number is an Armstrong number and `False` otherwise. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
"""

def is_armstrong_number(num):
    digits = [int(x) for x in str(num)]
    sum_ = 0
    for digit in digits:
        sum_ += pow(digit, len(digits))
    return num == sum_