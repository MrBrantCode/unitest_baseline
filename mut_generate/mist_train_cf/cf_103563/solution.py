"""
QUESTION:
Create a function named `sum_of_primes` that calculates the sum of all prime numbers within a given range, from 1 to n (inclusive), where n is 1000 in this case.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in range(1, n + 1) if is_prime(num))