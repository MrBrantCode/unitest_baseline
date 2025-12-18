"""
QUESTION:
Implement a function named `sort_composite_descending` that takes a list of integers as input, removes duplicates, skips any prime numbers, sorts the remaining composite numbers in descending order, and returns the sorted list.
"""

def sort_composite_descending(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    arr = list(set(arr))
    arr = [x for x in arr if not is_prime(x)]
    return sorted(arr, reverse=True)