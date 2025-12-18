"""
QUESTION:
Create a function `append_primes(listA, listB)` that takes two lists of integers `listA` and `listB` as input. The function should filter `listB` to include only prime numbers, sort them in descending order, remove duplicates from both lists, merge them into one list, sort the merged list in ascending order, and ensure the total number of elements does not exceed 1000. The function should have a time complexity of O(n log n), where n is the length of the resulting list.
"""

import math

def entance(listA, listB):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = sorted(set([x for x in listB if is_prime(x)]), reverse=True)
    merged_list = sorted(set(listA + primes))
    return merged_list[:1000]