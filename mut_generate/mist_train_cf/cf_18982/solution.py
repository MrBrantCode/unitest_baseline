"""
QUESTION:
Write a function named `prime_tuples` that takes a list of integers as input and returns a list of tuples, where each tuple contains the integer and a boolean value indicating if the integer is prime. The function should handle negative integers and zero, returning False for such values, and have a time complexity of O(n√m), where n is the number of integers in the input list and m is the maximum integer in the list.
"""

from typing import List, Tuple

def prime_tuples(numbers: List[int]) -> List[Tuple[int, bool]]:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [(num, is_prime(num)) if num > 1 else (num, False) for num in numbers]