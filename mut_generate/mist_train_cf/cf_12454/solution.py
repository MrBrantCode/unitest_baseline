"""
QUESTION:
Write a function `kth_smallest_prime(nums, k)` that finds the kth smallest prime number in an unsorted list of positive integers `nums`. The function should return `None` if there are less than `k` prime numbers in the list. The function `is_prime(num)` can be used to check if a number is prime.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def kth_smallest_prime(nums, k):
    primes = sorted([num for num in nums if is_prime(num)])
    return primes[k - 1] if len(primes) >= k else None