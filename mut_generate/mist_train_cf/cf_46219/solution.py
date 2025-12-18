"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers and a threshold as input. The function should return a new list where all duplicate elements (i.e., elements that appear more than once), elements that occur more than the specified threshold number of times, and prime numbers are removed. The order of the remaining elements in the output list should be the same as in the input list.
"""

from typing import List
from collections import Counter

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]:
    """ From a list of integers, remove duplicate elements, elements that occur more 
    than a specified number of times and prime numbers.
    Keep order of elements left the same as in the input.
    """
    frequency = Counter(numbers)
    non_duplicates = [number for number in numbers if frequency[number] == 1 and frequency[number] <= threshold and not is_prime(number)]
    return non_duplicates