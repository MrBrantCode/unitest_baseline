"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers within a given range. The function should take two integer parameters, `start` and `end`, representing the inclusive range within which to find and sum the prime numbers. The function should return the sum of all prime numbers within the specified range. If no prime numbers are found within the range, the function should return 0.
"""

def sum_of_primes(start: int, end: int) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum