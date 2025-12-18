"""
QUESTION:
Create a function `is_prime_with_two_factors(n)` that takes an integer `n` as input and returns a boolean indicating whether `n` is prime and has exactly two distinct prime factors.
"""

def is_prime_with_two_factors(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_prime_factors(num):
        count = 0
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 and is_prime(i):
                count += 1
                while num % i == 0:
                    num //= i
        if num > 1:
            count += 1
        return count

    return is_prime(n) and count_prime_factors(n) == 2