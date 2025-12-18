"""
QUESTION:
Create a Python function named `find_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The prime numbers in the output list should be in the same order as they appear in the input list.
"""

from typing import List

def find_primes(nums: List[int]) -> List[int]:
    primes = []
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes