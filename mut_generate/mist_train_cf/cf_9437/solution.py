"""
QUESTION:
Write a function named `find_primes` that takes an integer `n` as input and returns a list of all prime numbers from 1 to `n` in descending order. The function should not take any other parameters.
"""

def find_primes(n):
    primes = []
    for num in range(1, n+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes