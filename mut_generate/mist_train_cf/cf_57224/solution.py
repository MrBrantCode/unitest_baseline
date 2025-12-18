"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers and an integer threshold as input, removes elements that exceed the specified occurrence threshold and prime numbers from the list, and returns the resulting list while maintaining the original order of the remaining elements. The function should be implemented using a helper function `is_prime` to check for prime numbers.
"""

from typing import List
from collections import Counter
from math import sqrt

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:  # Exclude the even numbers > 2
        return False
    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]:
    """From a list of integers, purge duplicate elements, elements that exceed a certain occurrence threshold, and prime numbers.
    Retain the original order of the remaining elements.
    """
    count = Counter(numbers)
    filter_numbers = set(k for k, v in count.items() if v > threshold)
    numbers = [x for x in numbers if x not in filter_numbers and not is_prime(x)]
    return numbers