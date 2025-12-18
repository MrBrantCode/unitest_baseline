"""
QUESTION:
Write a function `solve(n)` that calculates the sum of the fifth-power values of all prime numbers within the range of 1 through to and including `n`. If the sum is odd, the function should also return the smallest prime number in the range that when added to the sum, makes it an even number. If the sum is even, the function should only return the sum.
"""

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

def solve(n):
    sum_primes = 0
    smallest_odd_prime = None
    for i in range(2, n+1):
        if is_prime(i):
            sum_primes += i**5
            if smallest_odd_prime is None and i % 2 != 0:
                smallest_odd_prime = i

    if sum_primes % 2 != 0:
        return (sum_primes, smallest_odd_prime)
    else:
        return (sum_primes,)