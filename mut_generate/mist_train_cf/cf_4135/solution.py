"""
QUESTION:
Write a function `max_difference(arr)` that takes an array of integers as input and returns the maximum difference between two elements in the array such that the larger element appears after the smaller element, the smaller element is at an odd index, the maximum difference is a prime number, and the smaller element is divisible by 3. If no such pair exists, return -1.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def max_difference(arr):
    max_diff = -1
    smallest_divisible_by_3 = float('inf')

    for i in range(1, len(arr), 2):
        if arr[i] % 3 == 0:
            smallest_divisible_by_3 = min(smallest_divisible_by_3, arr[i])
        else:
            if arr[i] > smallest_divisible_by_3:
                diff = arr[i] - smallest_divisible_by_3
                if is_prime(diff):
                    max_diff = max(max_diff, diff)

    return max_diff