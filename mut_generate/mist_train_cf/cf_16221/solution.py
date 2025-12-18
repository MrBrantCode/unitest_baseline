"""
QUESTION:
Given an array of integers, write a function called `find_indices` that returns the indices of elements that are both prime numbers and divisible by 3, with no duplicates, in a sorted list. The function must have a time complexity of O(n), where n is the length of the array.
"""

def find_indices(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    indices = set()
    for i, num in enumerate(arr):
        if num % 3 == 0 and is_prime(num):
            indices.add(i)
    return sorted(list(indices))