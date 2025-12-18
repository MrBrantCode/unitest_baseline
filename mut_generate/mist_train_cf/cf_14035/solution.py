"""
QUESTION:
Write a function `max_prime_subarray_sum` that takes two inputs: `arr`, an array of integers, and `k`, the length of the subarray. The function should return the maximum sum of a subarray of length `k` that consists only of prime numbers. Assume `k` is a positive integer and `arr` contains at least `k` prime numbers.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def max_prime_subarray_sum(arr, k):
    """Return the maximum sum of a subarray of length k that consists only of prime numbers."""
    primes = [num for num in arr if is_prime(num)]
    if len(primes) < k:
        return 0

    max_sum = 0
    window_sum = sum(primes[:k])

    max_sum = max(max_sum, window_sum)

    for i in range(k, len(primes)):
        window_sum = window_sum - primes[i - k] + primes[i]
        max_sum = max(max_sum, window_sum)

    return max_sum