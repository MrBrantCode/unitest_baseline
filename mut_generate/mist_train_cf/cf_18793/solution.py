"""
QUESTION:
Create a function `print_prime_numbers(n)` that prints all prime numbers between 0 and `n` (inclusive) using a while loop with a time complexity of O(sqrt(n)) and a space complexity of O(1). The function should handle inputs up to 1 million.
"""

import math

def print_prime_numbers(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    num = 2
    while num <= n:
        if is_prime(num):
            print(num)
        num += 1