"""
QUESTION:
Create a function `prime_numbers_between(start_range, end_range)` that takes two integers `start_range` and `end_range` as arguments and returns a list of all prime numbers between them (inclusive). The function should also calculate and return the total count of prime numbers and the sum of those prime numbers. The numbers in the returned list should be in ascending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_between(start_range, end_range):
    """
    Returns a list of all prime numbers between start_range and end_range (inclusive),
    along with their count and sum.

    Args:
        start_range (int): The start of the range (inclusive).
        end_range (int): The end of the range (inclusive).

    Returns:
        list: A list of prime numbers in the given range.
        int: The count of prime numbers in the given range.
        int: The sum of prime numbers in the given range.
    """
    prime_nums = []
    for num in range(start_range, end_range + 1):
        if is_prime(num):
            prime_nums.append(num)
    return prime_nums, len(prime_nums), sum(prime_nums)