"""
QUESTION:
Create a function `sum_of_prime_numbers(n)` that calculates the sum of the first `n` prime numbers, where `n` is a positive integer. If `n` is not a positive integer, return an error message. The function should be able to handle large values of `n` efficiently.
"""

import math

def sum_of_prime_numbers(n):
    if not isinstance(n, int) or n <= 0:
        return "n must be a positive integer."
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    prime_sum = 0
    num = 2
    
    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1
    
    return prime_sum