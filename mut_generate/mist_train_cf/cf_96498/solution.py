"""
QUESTION:
Write a function `calculate_sum_and_check_prime` that takes two positive integers `m` and `n` as input. The function should calculate the sum of all even integers in the range of `m` to `n` (inclusive), check if the sum is a prime number, and return the sum and a boolean indicating whether it is prime or not.
"""

def calculate_sum_and_check_prime(m, n):
    """
    Calculate the sum of all even integers in the range of m to n (inclusive) and 
    check if the sum is a prime number.

    Args:
    m (int): The start of the range.
    n (int): The end of the range.

    Returns:
    tuple: A tuple containing the sum of even numbers and a boolean indicating 
    whether the sum is prime or not.
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    sum_of_evens = sum(num for num in range(m, n + 1) if num % 2 == 0)
    return sum_of_evens, is_prime(sum_of_evens)