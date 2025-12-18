"""
QUESTION:
Write a recursive function `generate_prime_numbers(n)` that returns a list of all prime numbers in the range from 0 to the given number `n`, excluding any prime numbers that contain the digit 5. The solution should have a time complexity of O(n log(log n)).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers(n):
    if n < 2:
        return []
    primes = generate_prime_numbers(n-1)
    if '5' not in str(n) and is_prime(n):
        primes.append(n)
    return primes