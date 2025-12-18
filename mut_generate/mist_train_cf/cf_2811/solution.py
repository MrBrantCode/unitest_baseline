"""
QUESTION:
Write a function `find_prime_numbers(n)` to find all prime numbers less than a given positive integer `n`. The function should use a while loop to iterate through the numbers and check for primality. The input `n` is a positive integer, and the output should be a list of prime numbers less than `n`.
"""

def find_prime_numbers(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while num < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes