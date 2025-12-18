"""
QUESTION:
Create a function `is_strong_prime(n)` that checks whether a given number `n` is a strong prime number or not. A strong prime number is a prime number that is greater than 1, not a perfect square, and not a multiple of any of the first 100 prime numbers. The function should not use any mathematical libraries or built-in functions to check for perfect squares or multiples of prime numbers, and its time complexity should be less than O(sqrt(n)).
"""

def is_strong_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    def is_perfect_square(x):
        if x < 0:
            return False
        sqrt_x = int(x ** 0.5)
        return sqrt_x * sqrt_x == x

    if n <= 1 or is_perfect_square(n):
        return False
    primes = []
    i = 2
    while len(primes) < 100:
        if is_prime(i):
            primes.append(i)
        i += 1
    for prime in primes:
        if n % prime == 0:
            return False
    return True