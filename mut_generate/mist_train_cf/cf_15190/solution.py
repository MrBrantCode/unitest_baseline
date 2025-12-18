"""
QUESTION:
Create a function named `sum_of_primes_in_range` to calculate the sum of all prime numbers within a given range (inclusive) from 1 to `n`. The function should return the sum of prime numbers between 1 and `n`. The input `n` is an integer greater than 0, and the output is also an integer.
"""

def sum_of_primes_in_range(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in range(1, n + 1) if is_prime(num))