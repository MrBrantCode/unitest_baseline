"""
QUESTION:
Write a function named `reverse_and_remove_duplicates` that takes an array of integers as input, reverses the array, removes any duplicate elements, and returns a dictionary with the counts of non-prime numbers in the reversed array. The function should preserve the original order of elements and exclude prime numbers from the output. It should also handle arrays with up to 1 million elements efficiently within a time complexity of O(n log n).
"""

import math
from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_and_remove_duplicates(arr):
    arr = list(set(arr))  # Remove duplicates
    arr = arr[::-1]  # Reverse the array
    
    non_prime_counts = Counter()
    for num in arr:
        if not is_prime(num):
            non_prime_counts[num] += 1

    return non_prime_counts