"""
QUESTION:
Write a function `get_primes_multiples_and_sort` that takes two lists of integers as input and returns a list of numbers that are either prime numbers or multiples of 5 from both lists. The returned list should be sorted in descending order and should not include any numbers less than 20.
"""

def get_primes_multiples_and_sort(list1: list, list2: list):
    """Return prime numbers and numbers that are multiples of 5 from both lists, combined and sorted in descending order."""

    def is_prime(n: int) -> bool:
        if n > 1 and all(n%i for i in range(2, int(n ** 0.5) + 1)):
            return True
        return False

    prime_and_multiple_numbers = [n for n in list1 + list2 if (is_prime(n) or n % 5 == 0) and n >= 20]
    return sorted(prime_and_multiple_numbers, reverse=True)