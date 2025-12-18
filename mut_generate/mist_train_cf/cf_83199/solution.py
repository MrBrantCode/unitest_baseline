"""
QUESTION:
Implement the function `prime_advanced_sum(n, k)` with the following requirements:

Given a positive integer `n` and `k`, return the cumulative sum of all `n`-digit prime numbers whose digit sum is prime, not divisible by 5, has an odd number of digits, and is not divisible by `k`. The solution should not use any built-in Python libraries for prime number computation and should aim for a reduced time complexity.
"""

def prime_advanced_sum(n, k):
    start = 10**(n-1)
    if start==1: start=2
    end = 10**n
    primes = [i for i in range(start, end) if is_prime(i) and i%k != 0]
    filtered_primes = [i for i in primes if is_prime(digits_sum(i)) and digits_sum(i)%5 != 0 and len(str(i)) % 2 == 1]
    return sum(filtered_primes)

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    

def digits_sum(n):
    return sum([int(i) for i in str(n)])