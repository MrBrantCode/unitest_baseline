"""
QUESTION:
Create a function `find_primes(n, m)` that takes two integers `n` and `m`, where `n` and `m` are inclusive, and returns a list of prime numbers between `n` and `m`. The function should return all prime numbers in the range, including `n` and `m` if they are prime.
"""

def is_prime(num):
    # Check if num is less than 2, it's not prime
    if num < 2:
        return False
    # Check if num is divisible by any number from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    # If num is not divisible by any number, it's prime
    return True

def find_primes(n, m):
    primes = []
    # Iterate through all numbers between n and m (inclusive)
    for num in range(n, m+1):
        if is_prime(num):
            primes.append(num)
    return primes