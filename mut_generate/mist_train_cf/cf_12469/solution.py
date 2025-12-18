"""
QUESTION:
Write a function `check_prime_division` that takes two integers `a` and `b` as input, performs integer division `a/b`, and checks if the resulting output is a prime number. The function should return a boolean indicating whether the output is prime or not. Note that the division should be performed as integer division (i.e., rounding down to the nearest whole number) and the input `b` is guaranteed to be non-zero.
"""

def check_prime_division(a, b):
    """
    Performs integer division a/b and checks if the resulting output is a prime number.

    Args:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    bool: True if the output is a prime number, False otherwise.
    """

    output = a // b  # Perform integer division

    # Check if the output is prime
    if output < 2:  # Numbers less than 2 are not prime
        return False

    for i in range(2, int(output ** 0.5) + 1):  # Only need to check up to sqrt(output)
        if output % i == 0:
            return False

    return True