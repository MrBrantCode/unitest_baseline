"""
QUESTION:
Write a function `max_difference(arr)` that takes an array of integers as input and returns the maximum difference between two elements in the array such that the larger element appears after the smaller element, the smaller element is at an odd index, and the difference is a prime number. The smaller element must also be divisible by 3. If no such pair exists, return -1.
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
            diff = arr[i] - smallest_divisible_by_3
            if is_prime(diff) and diff > max_diff:
                max_diff = diff

    for i in range(0, len(arr), 2):
        if arr[i] % 3 == 0:
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i] and is_prime(arr[j] - arr[i]):
                    max_diff = max(max_diff, arr[j] - arr[i])

    return max_diff