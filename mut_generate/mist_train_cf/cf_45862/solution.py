"""
QUESTION:
Implement a function `remove_duplicates(numbers, threshold)` that takes a list of integers and strings, and an integer threshold. The function should return a new list where duplicate integers, integers that appear more than the specified threshold, and prime numbers are removed, while preserving the original order of the remaining elements. The function should not affect string-type elements in the list.
"""

from typing import List, Union
from collections import Counter

def is_prime(n: int) -> bool:
    """Check if an integer is a prime number"""
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def remove_duplicates(numbers: List[Union[int, str]], threshold: int) -> List[Union[int, str]]:
    """Implement a function to process a collection of integers and strings, purging duplicate integers, components exceeding a particular presence limit, and prime numbers.
    It is crucial to retain the ordinal sequence of the remaining elements as seen in the input.
    """
    counter = Counter()
    result = []
    for num in numbers:
        if isinstance(num, int):
            if not is_prime(num):
                counter[num] += 1
                if counter[num] <= threshold:
                    result.append(num)
        else:
            result.append(num)
    return result