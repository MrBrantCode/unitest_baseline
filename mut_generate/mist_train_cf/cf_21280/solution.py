"""
QUESTION:
Create a function called `next_n_primes` that takes an integer `n` as input and returns an array of the next `n` prime numbers after the largest prime number less than `n`. The function should work for any non-negative integer `n`.
"""

def next_n_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = n + 1
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes