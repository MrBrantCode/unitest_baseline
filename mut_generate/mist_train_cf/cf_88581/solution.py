"""
QUESTION:
Create a function named `odd_sum_multiple` that takes a single positive integer `n` as input and returns the sum of all odd numbers from 1 to `n` multiplied by 3. However, if `n` is a prime number, the sum should be multiplied by 4 instead. The function should also handle non-positive integers by returning an error message stating that only positive numbers are allowed.
"""

import math

def odd_sum_multiple(n):
    if n < 1:
        return "Only positive numbers are allowed."
    
    odd_sum = sum(i for i in range(1, n+1) if i % 2 != 0)
    
    if n > 1:
        is_prime = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
    else:
        is_prime = False

    return odd_sum * 4 if is_prime else odd_sum * 3