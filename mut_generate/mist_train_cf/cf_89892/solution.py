"""
QUESTION:
Create a function `generate_prime_matrix(n, m)` that generates a 2-dimensional array of size `n` by `m` containing all prime numbers where `n` and `m` are prime numbers greater than 2. The function should return a 2D array where each row contains `m` prime numbers, and the prime numbers are generated in ascending order.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_matrix(n, m):
    primes = []
    num = 2
    while len(primes) < n * m:
        if is_prime(num):
            primes.append(num)
        num += 1
    prime_matrix = [primes[i*m:(i+1)*m] for i in range(n)]
    return prime_matrix