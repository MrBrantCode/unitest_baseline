"""
QUESTION:
Create a function named 'list_primes' that takes an integer 'n' as input and returns a list of all prime numbers less than 'n' along with the sum of these prime numbers.
"""

def list_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n) if is_prime(i)]
    return primes, sum(primes)