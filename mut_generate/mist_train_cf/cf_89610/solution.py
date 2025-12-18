"""
QUESTION:
Create a function called "largest_common_divisor" that takes two positive integers A and B as input and returns the largest common divisor between A and B. The solution should not use any built-in functions or libraries for calculating the greatest common divisor or the Euclidean algorithm. The time complexity of the solution should be O(N), where N is the number of prime factors in the smaller of the two input numbers.
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

    result = 1

    for prime_factor in prime_factors:
        if A % prime_factor == 0 and B % prime_factor == 0:
            result *= prime_factor

    return result