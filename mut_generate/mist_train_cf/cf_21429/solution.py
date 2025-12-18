"""
QUESTION:
Implement a function called `sum_primes` that calculates the sum of all prime numbers up to a given number `n`. The function should return the sum as the output. The solution should have a time complexity of O(n log log n) or better, and it is recommended to use an optimized algorithm such as the Sieve of Eratosthenes.
"""

def sum_primes(n):
    if n <= 1:
        return 0

    # Initialize a list to keep track of prime numbers
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    # Use Sieve of Eratosthenes algorithm to mark non-prime numbers
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    # Calculate the sum of prime numbers
    prime_sum = 0
    for num in range(2, n+1):
        if primes[num] == True:
            prime_sum += num

    return prime_sum