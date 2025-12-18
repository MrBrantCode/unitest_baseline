"""
QUESTION:
Create a function `sum_primes(n)` that takes an integer `n` as an argument and returns the sum of all prime numbers from 1 to `n`. The function should have a time complexity of O(n²) and should not use any built-in functions or libraries to check for prime numbers. The function should also not use the Sieve of Eratosthenes algorithm or any other algorithm that can determine prime numbers in O(n log log n) time complexity.
"""

def sum_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum