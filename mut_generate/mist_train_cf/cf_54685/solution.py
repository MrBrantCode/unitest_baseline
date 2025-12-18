"""
QUESTION:
Create a function called `is_prime_sum_odd` to calculate the sum of squares of all prime numbers up to a given number `n`, and return `True` if the sum is odd, `False` otherwise. The function should not take any other arguments besides `n`.
"""

import itertools

def is_prime_sum_odd(n):
    """Check if the sum of squares of all prime numbers up to n is odd"""
    sum = 0
    for i in range(n):
        if i < 2:
            continue
        is_prime = True
        for j in itertools.islice(itertools.count(2), int(i**0.5 - 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            sum += i ** 2
            
    return sum % 2 != 0