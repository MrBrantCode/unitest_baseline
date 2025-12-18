"""
QUESTION:
Create a function called `sum_of_primes` that takes an array of positive integers as input and returns the sum of prime numbers in the array. Consider a prime number as a positive integer greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def sum_of_primes(input_array):
    prime_sum = 0

    for num in input_array:
        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_sum += num

    return prime_sum