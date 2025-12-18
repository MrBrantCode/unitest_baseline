"""
QUESTION:
Create a function `generate_prime_multiplication_table` that generates a 5x5 multiplication table for the first 5 prime numbers within a given range. The function should take a range (start and end) as input and return the multiplication table. The prime numbers should be selected from the range [start, end] and the table should be generated using these prime numbers. Optimize the code to minimize time complexity.
"""

import math

def generate_prime_multiplication_table(start, end):
    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    prime_numbers = prime_numbers[:5]  # Select the first 5 prime numbers

    table = [[i * j for j in prime_numbers] for i in prime_numbers]
    return table