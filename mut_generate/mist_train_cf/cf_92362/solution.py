"""
QUESTION:
Write a function named `find_primes` that finds all prime numbers below a given number n. The function should iterate through numbers from 2 to n-1 and return a list of all prime numbers found.
"""

def find_primes(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes