"""
QUESTION:
Write a function called `primes_greater_than_X` that takes a list of integers `lst` and a target integer `X` as input, and returns a tuple containing a list of all prime numbers in `lst` that are greater than `X` and the count of these qualifying prime numbers.
"""

def primes_greater_than_X(lst, X):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for div in range(3, max_div, 2):
            if n % div == 0:
                return False
        return True

    primes = [num for num in lst if num > X and is_prime(num)]
    return primes, len(primes)