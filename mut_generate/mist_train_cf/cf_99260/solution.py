"""
QUESTION:
Create a function `count_prime_factors(num)` that takes an integer `num` as input, returns the number of prime factors of `num`, its binary representation, and the number of bits used. If `num` is negative, return an error message. The function should handle integers only.
"""

import math
def count_prime_factors(num):
    if num < 0:
        return "Error: Input value must be a positive integer"
    elif num == 0 or num == 1:
        return "Number of prime factors: 0"
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
        return f"Number of prime factors: {num_prime_factors}\nBinary representation: {binary}\nNumber of bits: {num_bits}"