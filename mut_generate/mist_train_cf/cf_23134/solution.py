"""
QUESTION:
Generate a function `get_prime_divisors_and_sum_of_squares(n)` that takes a number `n` as input and returns a list containing the list of all prime divisors of `n` and the sum of their squares.
"""

import math

def get_prime_divisors_and_sum_of_squares(n):
    prime_divisors = []
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_divisors.append(i)
                
    sum_squares = sum(divisor**2 for divisor in prime_divisors)
    
    return prime_divisors, sum_squares