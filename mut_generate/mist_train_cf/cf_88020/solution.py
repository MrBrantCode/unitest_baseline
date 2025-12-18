"""
QUESTION:
Write a program with the following functions: 

- `is_prime(n)`: checks if a number is prime.
- `find_sum_of_primes()`: returns the sum of the first 1000 prime numbers greater than 100.
- `find_square_of_sum()`: returns the square of the sum of the first 1000 prime numbers greater than 100.
- `find_largest_prime()`: returns the largest prime number less than the square of the sum.

The program should output the square of the sum and the largest prime number.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_sum_of_primes():
    primes = []
    num = 101  # Start checking from 101, as we want primes greater than 100

    while len(primes) < 1000:
        if is_prime(num):
            primes.append(num)
        num += 1

    return sum(primes)

def find_square_of_sum():
    sum_of_primes = find_sum_of_primes()
    return sum_of_primes ** 2

def find_largest_prime():
    square_of_sum = find_square_of_sum()
    largest_prime = 0

    for i in range(square_of_sum - 1, 1, -1):
        if is_prime(i):
            largest_prime = i
            break

    return largest_prime