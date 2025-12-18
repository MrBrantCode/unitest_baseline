"""
QUESTION:
Create a function `divisible_by_5_and_sum_of_digits_divisible_by_3(number)` that takes an integer `number` as input and returns a boolean value. The function should return `True` if the number is divisible by 5 and the sum of its digits is also divisible by 3, otherwise it should return `False`.
"""

def divisible_by_5_and_sum_of_digits_divisible_by_3(number):
    if number % 5 == 0:  # Check if number is divisible by 5
        digit_sum = sum([int(digit) for digit in str(number)])  # Calculate sum of digits
        if digit_sum % 3 == 0:  # Check if sum of digits is divisible by 3
            return True
    return False