"""
QUESTION:
Write a function named `multiply_abs_values` that takes a list of numbers as input. The function should return the product of the absolute values of the numbers in the list after removing the perfect squares, perfect cubes, and numbers divisible by any prime numbers less than or equal to 10. Use a helper function named `find_prime` to check if a number is prime.
"""

import math

def find_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def multiply_abs_values(lst):
    primes_less_than_10 = [i for i in range(2, 11) if find_prime(i)]
    product = 1
    for num in lst:
        num = abs(math.floor(num))
        num_cubert = round(num**(1/3))
        num_sqrt = round(math.sqrt(num))
        if num == num_cubert ** 3:
            num = num_cubert
        elif num == num_sqrt ** 2:
            num = num_sqrt
        if any(num % prime == 0 for prime in primes_less_than_10):
            continue
        product *= num
    return product