"""
QUESTION:
Create a function called "largest_common_divisor" that takes two positive integers A and B as input and returns their largest common divisor without using any built-in functions or libraries for calculating the greatest common divisor. The function should have a time complexity of O(N), where N is the number of prime factors in the smaller of the two input numbers, and should not use the Euclidean algorithm or any other well-known algorithm for calculating the greatest common divisor.
"""

import math

def largest_common_divisor(A, B):
    smaller_number = min(A, B)
    prime_factors = []

    for i in range(2, int(math.sqrt(smaller_number)) + 1):
        while smaller_number % i == 0:
            prime_factors.append(i)
            smaller_number //= i

    if smaller_number > 1:
        prime_factors.append(smaller_number)

    largest_common_divisor = 1

    for prime_factor in prime_factors:
        if A % prime_factor == 0 and B % prime_factor == 0:
            largest_common_divisor *= prime_factor

    return largest_common_divisor