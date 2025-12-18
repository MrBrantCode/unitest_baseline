"""
QUESTION:
Write a function `kth_smallest_prime(nums, k)` that takes a list of positive integers `nums` and an integer `k` as inputs, and returns the kth smallest prime number from the list. If there are less than k prime numbers in the list, the function should return `None`.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def kth_smallest_prime(nums, k):
    primes = [num for num in nums if is_prime(num)]
    primes.sort()
    if len(primes) < k:
        return None
    return primes[k - 1]