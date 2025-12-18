"""
QUESTION:
Create a function `sum_of_primes` that calculates and returns the sum of all prime numbers less than or equal to a given input number `n`. The function should utilize the helper function `is_prime` to check if a number is prime or not.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(i for i in range(2, n+1) if is_prime(i))