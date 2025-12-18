"""
QUESTION:
Create a function `find_primes(upper_bound)` that returns a list of all prime numbers between 2 and the given `upper_bound`. The function should check each number in the range for primality and return a list of all prime numbers found.
"""

def find_primes(upper_bound):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    primes = []
    for n in range(2, upper_bound + 1):
        if is_prime(n):
            primes.append(n)
    return primes