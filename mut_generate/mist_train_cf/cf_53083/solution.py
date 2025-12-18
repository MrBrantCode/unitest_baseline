"""
QUESTION:
Build a function `prime_square_diff` that constructs a matrix where each row represents a prime number, its square, and the difference between its square and the square of the previous prime number. The function should take an integer `prime_num` as input, which specifies the upper limit for the prime numbers. The function should return a 2D list (or matrix) where each row is in the format `[prime, prime_square, diff]`. The `diff` value for the first row should be 0.
"""

def prime_square_diff(prime_num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [p for p in range(2, prime_num + 1) if is_prime(p)]
    matrix = []

    for i in range(len(primes)):
        prime_square = primes[i] ** 2
        if i == 0:
            diff = 0
        else:
            diff = prime_square - (primes[i-1] ** 2)
        matrix.append([primes[i], prime_square, diff])

    return matrix