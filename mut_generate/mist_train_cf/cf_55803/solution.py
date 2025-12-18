"""
QUESTION:
Write a function `generate_n_primes(n)` that generates the first n prime numbers. The function should start from the smallest prime number, which is 2, and iterate over positive integers to check for primality. The primality check should be performed by trying to divide each number by all smaller numbers up to the square root of the number. If a number can be divided without any remainder, it is not a prime number. The function should continue this process until it finds n prime numbers. The function should return a list of the first n prime numbers. 

Note: The input n is a positive integer and the function should be efficient.
"""

def generate_n_primes(n):
    primes = []
    i = 2 

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes