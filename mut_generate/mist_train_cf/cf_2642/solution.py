"""
QUESTION:
Create a function `reverse_and_remove_duplicates` that takes an array of integers as input, reverses the array, removes any duplicate elements while preserving the original order, and ensures the reversed array does not contain any prime numbers. The function should return a dictionary containing the count of each non-prime number in the reversed array. The input array can contain up to 1 million elements and the time complexity of the solution should be O(n log n).
"""

import math
from collections import Counter

def reverse_and_remove_duplicates(arr):
    arr = list(set(arr))  # Remove duplicates
    arr = arr[::-1]  # Reverse the array
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    non_prime_counts = Counter()
    for num in arr:
        if not is_prime(num):
            non_prime_counts[num] += 1

    return non_prime_counts