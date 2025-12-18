"""
QUESTION:
Given a list of integers and an integer k, write a function `kth_smallest_prime` that returns the kth smallest prime number in the list, considering only unique positive integers. The function should ignore duplicate and negative numbers. If k is greater than the number of primes found, return None.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def kth_smallest_prime(numbers, k):
    primes = set()
    for num in numbers:
        if num > 0 and is_prime(num):
            primes.add(num)
    sorted_primes = sorted(primes)
    if k <= len(sorted_primes):
        return sorted_primes[k-1]
    else:
        return None