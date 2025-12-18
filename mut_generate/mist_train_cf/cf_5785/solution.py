"""
QUESTION:
Create a function `find_primes_and_digit_sums` that takes two positive integers `m` and `n` as input and returns a list of prime numbers between `m` and `n`, along with the sum of their digits and whether the sum is also a prime number. The function should return a list of tuples, where each tuple contains the prime number, the sum of its digits, and a boolean indicating whether the sum is prime.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))


def find_primes_and_digit_sums(m, n):
    """
    Find prime numbers between m and n, along with the sum of their digits and 
    whether the sum is also a prime number.

    Args:
        m (int): The lower bound (inclusive).
        n (int): The upper bound (inclusive).

    Returns:
        list[tuple]: A list of tuples, where each tuple contains the prime number, 
        the sum of its digits, and a boolean indicating whether the sum is prime.
    """
    result = []
    for num in range(m, n + 1):
        if is_prime(num):
            digit_sum = sum_of_digits(num)
            is_digit_sum_prime = is_prime(digit_sum)
            result.append((num, digit_sum, is_digit_sum_prime))
    return result