"""
QUESTION:
Create a function named `count_prime_factors(num)` that takes an integer as input and returns the number of prime factors, the binary representation, and the number of bits used. The function should handle negative input values by returning an error message and handle non-integer inputs by truncating them to integers. The function should also be able to handle edge cases such as 0 and 1, where the number of prime factors is 0.
"""

import math

def count_prime_factors(num):
    num = int(num)
    if num < 0:
        return "Error: Input value must be a positive integer"
    elif num == 0 or num == 1:
        return 0, bin(num)[2:], len(bin(num)[2:])
    else:
        binary = bin(num)[2:]
        num_bits = len(binary)
        prime_factors = set()
        while num % 2 == 0:
            prime_factors.add(2)
            num //= 2
        for i in range(3, int(math.sqrt(num))+1, 2):
            while num % i == 0:
                prime_factors.add(i)
                num //= i
        if num > 2:
            prime_factors.add(num)
        num_prime_factors = len(prime_factors)
        return num_prime_factors, binary, num_bits