"""
QUESTION:
Implement a function named `sum_unique_primes` that takes an array of integers as input and returns the sum of unique prime elements in the array. The function should consider each prime number only once even if it appears multiple times in the array.
"""

def sum_unique_primes(array):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    unique_primes = set()
    for num in array:
        if is_prime(num) and num not in unique_primes:
            unique_primes.add(num)
    return sum(unique_primes)