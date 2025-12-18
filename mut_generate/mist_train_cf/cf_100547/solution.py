"""
QUESTION:
Write a function `is_narcissistic` that takes an integer `num` as input and returns a boolean indicating whether the number is narcissistic, i.e., the sum of the Nth power of each digit is equal to the number itself, where N is the number of digits in `num`. The function should be able to handle integers with any number of digits.
"""

def is_narcissistic(num):
    # convert the number to a string and get the length
    num_str = str(num)
    n = len(num_str)
    # calculate the sum of the Nth power of each digit
    sum_digits = sum(int(digit)**n for digit in num_str)
    # return True if the sum is equal to the number
    return num == sum_digits