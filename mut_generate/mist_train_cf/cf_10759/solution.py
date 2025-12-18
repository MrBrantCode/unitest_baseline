"""
QUESTION:
Write a function `sum_of_squares_of_primes` to compute the sum of the squares of all the prime numbers between 1 and a given number n (inclusively). The input is an integer n, and the output is the sum of the squares of all the prime numbers between 1 and n.
"""

def sum_of_squares_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum([i**2 for i in range(1, n+1) if is_prime(i)])