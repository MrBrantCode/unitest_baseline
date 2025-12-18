"""
QUESTION:
Write a function `digit_sum_product` that takes a list of digit strings as input. The function should concatenate the digit strings into a single continuous integer and then calculate the sum of its digits. Return both the continuous integer and the sum of its digits. The input list will only contain single-character digit strings.
"""

def digit_sum_product(lst):
    # Transform digit strings into a continuous integer
    continuous_int = int("".join(lst))

    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(continuous_int))

    return continuous_int, digit_sum