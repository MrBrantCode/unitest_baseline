"""
QUESTION:
Write a function named `kth_smallest_prime` that takes two inputs: `numbers` and `k`, where `numbers` is a list of integers and `k` is a positive integer. The function should return the kth smallest prime number in the list, ignoring non-positive numbers and duplicates. If k is greater than the number of primes found, the function should return None.
"""

def kth_smallest_prime(numbers, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = set()
    for num in numbers:
        if num > 0 and is_prime(num):
            primes.add(num)
    sorted_primes = sorted(primes)
    if k <= len(sorted_primes):
        return sorted_primes[k-1]
    else:
        return None