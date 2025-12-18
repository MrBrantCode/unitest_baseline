"""
QUESTION:
Create a function `find_primes` that takes an integer `n` as input and returns a list of all prime numbers from 1 to `n`. The function must use a single loop and have a time complexity of O(n).
"""

def find_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    
    for num in range(2, n + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num, n + 1, num):
                sieve[i] = False
    
    return primes