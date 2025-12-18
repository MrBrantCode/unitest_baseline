"""
QUESTION:
Create a function called `even_prime_numbers(limit)` that returns a list of even prime numbers from 2 up to a given `limit`, where `limit` does not exceed 1000. Then, find the cumulative sum of these even prime numbers and return it.
"""

def even_prime_numbers(limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True

    even_primes = [i for i in range(2, limit+1) if is_prime(i) and i%2 == 0]
    cum_sum = sum(even_primes)
    return cum_sum