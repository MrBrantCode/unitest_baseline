"""
QUESTION:
Write a function `is_prime_and_index_and_digit_sum_valid` that takes an integer `n` and its index `i` in an array as input. The function should return `True` if `n` is a prime number, `i` is a multiple of 3, and the sum of the digits of `n` is divisible by 5, otherwise return `False`.
"""

def is_prime_and_index_and_digit_sum_valid(n, i):
    """
    Checks if a number is prime, its index is a multiple of 3, and the sum of its digits is divisible by 5.

    Args:
    n (int): The number to be checked.
    i (int): The index of the number in the array.

    Returns:
    bool: True if the number is prime, its index is a multiple of 3, and the sum of its digits is divisible by 5, False otherwise.
    """

    # Check if index is a multiple of 3
    if i % 3 != 0:
        return False

    # Check if number is prime
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False

    # Check if sum of digits is divisible by 5
    digit_sum = sum(int(digit) for digit in str(n))
    if digit_sum % 5 != 0:
        return False

    return True