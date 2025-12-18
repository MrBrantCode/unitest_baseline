"""
QUESTION:
Write a function `find_primes(N)` that takes a positive integer `N` as input and returns a list of all prime numbers from 1 to `N`. The function should have a time complexity of O(N√N) and not use any built-in functions or libraries that directly solve this problem.
"""

def find_primes(N):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(2, N+1):
        if is_prime(i):
            primes.append(i)
    return primes