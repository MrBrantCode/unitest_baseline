"""
QUESTION:
Write a function `sum_of_cubes_of_primes(n)` that calculates the sum of the cube of prime numbers from 1 to n, where n is a positive integer. The function should have a time complexity of O(n) and should not use any built-in functions or libraries to determine if a number is prime.
"""

def sum_of_cubes_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    sum = 0
    for i in range(1, n + 1):
        if is_prime(i):
            sum += i**3
    return sum