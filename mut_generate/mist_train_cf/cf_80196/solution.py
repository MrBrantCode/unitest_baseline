"""
QUESTION:
Write a function called `find_primes` that takes an array of integers as input and returns the smallest and largest prime numbers in the array. If no prime numbers are present in the array, the function should return `None` for both values. The input array may contain integers ranging from 1 to 500.
"""

def find_primes(array):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in array if is_prime(i)]
    if not primes:
        return None, None
    return min(primes), max(primes)