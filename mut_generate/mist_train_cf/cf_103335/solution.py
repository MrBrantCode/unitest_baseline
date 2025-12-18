"""
QUESTION:
Write a function `check_divisible_by_5_and_sum_of_digits` that takes a single integer `num` as input. This integer should be greater than or equal to 10 and less than or equal to 10^6. The function should return a tuple containing a boolean indicating whether `num` is divisible by 5 and the sum of all the digits in `num`.
"""

def check_divisible_by_5_and_sum_of_digits(num):
    """
    Checks if a number is divisible by 5 and calculates the sum of its digits.

    Args:
        num (int): A positive integer between 10 and 10^6.

    Returns:
        tuple: A tuple containing a boolean indicating whether num is divisible by 5 and the sum of its digits.
    """
    is_divisible_by_5 = num % 5 == 0
    sum_of_digits = sum(int(digit) for digit in str(num))
    return is_divisible_by_5, sum_of_digits