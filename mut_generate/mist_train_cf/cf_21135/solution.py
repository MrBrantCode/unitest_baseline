"""
QUESTION:
Write a function named `remove_primes` that takes an array of integers as input and returns the sum of the remaining numbers in the array after removing all prime numbers.
"""

def remove_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    non_prime_sum = 0
    for num in arr:
        if not is_prime(num):
            non_prime_sum += num
    return non_prime_sum