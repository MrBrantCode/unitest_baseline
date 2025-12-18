"""
QUESTION:
Write a function called `generate_primes` that generates a specified number of distinct prime numbers within a given range. The function should take three parameters: `start`, `end`, and `count`, representing the start of the range, the end of the range, and the number of primes to generate, respectively. The function should return a list of distinct prime numbers.
"""

def generate_primes(start, end, count):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
        if len(primes) == count:
            break
    return primes