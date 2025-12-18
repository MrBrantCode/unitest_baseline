"""
QUESTION:
Write a function `generate_prime_matrix(n, m)` that returns a 2-dimensional array of size n by m, containing all prime numbers within the range 1 to n*m. Here, n and m are prime numbers greater than 2. The function should use a helper function `is_prime(num)` to check if a number is prime. The generated matrix should contain prime numbers in a row-major order, starting from the smallest prime number.

Restrictions:
- n and m are prime numbers greater than 2.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_matrix(n, m):
    count = 0
    primes = []
    num = 1
    while len(primes) < n * m:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    prime_matrix = [primes[i:i+m] for i in range(0, len(primes), m)]
    return prime_matrix