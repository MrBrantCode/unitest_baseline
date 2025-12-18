"""
QUESTION:
Create a function `append_primes(listA, listB)` that takes two lists `listA` and `listB` as input. The function should append the prime numbers from `listB` to `listA`, ensuring the resulting list is sorted in ascending order and contains no duplicates. The total number of elements in the resulting list must not exceed 1000. The algorithm should have a time complexity of O(n log n), where n is the length of the resulting list.
"""

import math

def append_primes(listA, listB):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in listB if is_prime(x)]
    primes = sorted(set(primes))
    result = sorted(set(listA + primes))
    return result[:1000]  # Ensure the total number of elements does not exceed 1000