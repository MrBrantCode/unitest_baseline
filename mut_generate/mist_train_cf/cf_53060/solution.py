"""
QUESTION:
Implement a function `get_even_prime_and_merge` that takes two lists of integers `l1` and `l2` as input. The function should return a list of even prime numbers from both input lists, merged and sorted in descending order. 

You are required to implement two helper functions `merge_and_sort` and `is_prime`. The `is_prime` function should check whether a given number is prime or not. The `merge_and_sort` function should merge two lists and sort the result in descending order. Ignore any non-positive integers and integers that are not even prime numbers. Ensure the function handles the edge case where the only even prime number is 2.
"""

def get_even_prime_and_merge(l1: list, l2: list):
    """Return only even prime numbers from both lists, merged and sorted in descending order.
    >>> get_even_prime_and_merge([1, 2, 3, 4, 5, 6], [2, 3, 5, 7, 11, 13])
    [2, 2]
    """

    def is_prime(x: int):
        """Check if a number is prime."""
        if x <= 1:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        max_divisor = int(x**0.5) + 1
        for d in range(3, max_divisor, 2):
            if x % d == 0:
                return False
        return True

    def merge_and_sort(m: list, n: list):
        """Merge two lists and sort the result in descending order."""
        return sorted(m + n, reverse=True)

    even_prime_numbers = []
    for num in l1 + l2:
        if num > 0 and num % 2 == 0 and is_prime(num):
            even_prime_numbers.append(num)

    return merge_and_sort([], even_prime_numbers)