"""
QUESTION:
Create a function named `is_armstrong_and_prime_number(n)` that takes an integer `n` as input and returns a tuple with two boolean values. The first value indicates whether `n` is an Armstrong number and the second value indicates whether `n` is a prime number. The function should handle integers of any size. The definition of an Armstrong number is a number that is equal to the sum of cubes of its digits. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def is_armstrong_and_prime_number(n):
    is_armstrong = False
    is_prime = False
    
    # Check for Armstrong number
    temp = n
    sum = 0
    order = len(str(n))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        is_armstrong = True

    # Check for prime number
    if n > 1:
        if n <= 3:
            is_prime = True
        elif n % 2 == 0 or n % 3 == 0:
            is_prime = False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
            else:
                is_prime = True
    
    return (is_armstrong, is_prime)