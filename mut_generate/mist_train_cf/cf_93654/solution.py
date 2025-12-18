"""
QUESTION:
Create a function named `divisors(num)` that takes an integer `num` as input and returns a list of its divisors, excluding 1 and `num` itself, in ascending order. The function should be optimized to have a time complexity of O(sqrt(n)), where n is the given number, and should handle numbers up to 10^9. If `num` is prime, the function should return an empty list.
"""

import math

def divisors(num):
    divisors_list = []
    sqrt_num = int(math.sqrt(num))

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisor = i
            quotient = num // i

            if divisor != quotient:
                divisors_list.append(divisor)
            divisors_list.append(quotient)

    return divisors_list