"""
QUESTION:
Design a class with a method `reverse(num)` that takes an integer `num` as input and returns the reverse of the number. The method should handle negative numbers by returning the reverse as a negative number. The method should also have a time complexity of O(log n), where n is the absolute value of the input number, and a space complexity of O(1).

Additionally, the class should have a method `sum_of_digits(num)` that returns the sum of the digits in the reversed number. The input number can be a positive or negative integer with a maximum absolute value of 10^9.
"""

def reverse(num):
    """
    This function takes an integer as input and returns its reverse.
    It handles negative numbers by returning the reverse as a negative number.
    The time complexity is O(log n) where n is the absolute value of the input number.
    The space complexity is O(1).

    Args:
        num (int): The input number.

    Returns:
        int: The reverse of the input number.
    """
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num //= 10
    return -rev if is_negative else rev

def sum_of_digits(num):
    """
    This function takes an integer as input and returns the sum of the digits in the reversed number.

    Args:
        num (int): The input number.

    Returns:
        int: The sum of the digits in the reversed number.
    """
    sum_digits = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        sum_digits += num % 10
        num //= 10
    return sum_digits