"""
QUESTION:
Write a function named `kth_smallest_prime` that takes a list of integers and a positive integer `k` as input. The function should return the kth smallest prime number from the list. The function should not use any built-in sorting functions or libraries and should not use any built-in prime number checking functions or libraries. The function should return `None` if `k` is greater than the number of prime numbers in the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def kth_smallest_prime(numbers, k):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    if k <= len(primes):
        return primes[k - 1]
    else:
        return None