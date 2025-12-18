"""
QUESTION:
Write a function `odd_sum_multiple(n)` that takes a positive integer `n` as input. The function should return the sum of all odd numbers from 1 to `n` multiplied by 3, unless `n` is a prime number, in which case the sum should be multiplied by 4. If `n` is not a positive integer, the function should return an error message.
"""

import math

def odd_sum_multiple(n):
    if n < 1:
        return "Only positive numbers are allowed."
    
    odd_sum = 0
    is_prime = True

    for i in range(1, n+1):
        if i % 2 != 0:
            odd_sum += i

    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        return odd_sum * 4
    else:
        return odd_sum * 3