"""
QUESTION:
Create a function called `find_primes(n, m)` that takes two integers, n and m, and returns a list of prime numbers between n and m (inclusive). The function should return all prime numbers in the range, including n and m if they are prime.
"""

def find_primes(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(n, m+1):
        if is_prime(num):
            primes.append(num)
    return primes