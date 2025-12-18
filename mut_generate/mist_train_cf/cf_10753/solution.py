"""
QUESTION:
Create a function named `prime_numbers_without_5(n)` that returns a list of prime numbers between 2 and 'n' (inclusive), excluding any numbers that contain the digit '5'. The function should work for values of 'n' up to 1000.
"""

import math

def prime_numbers_without_5(n):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    prime_numbers = []
    for number in range(2, n + 1):
        if '5' in str(number):
            continue
        if is_prime(number):
            prime_numbers.append(number)
    
    return prime_numbers