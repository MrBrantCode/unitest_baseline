"""
QUESTION:
Create a function called `sum_of_prime_numbers` that takes a single integer `n` as input. The function should return the sum of the first `n` prime numbers. If `n` is not a positive integer, return the error message "n must be a positive integer." The function should be able to handle large values of `n` efficiently (e.g., greater than 10^6).
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