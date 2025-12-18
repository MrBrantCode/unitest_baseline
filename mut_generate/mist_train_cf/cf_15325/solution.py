"""
QUESTION:
Create a function `divisors(num)` that takes an integer `num` and returns a list of its divisors excluding 1 and the number itself in ascending order. The function should be able to handle numbers up to 10^9 and return an empty list if the number is prime. Optimize the function to have a time complexity of O(sqrt(n)), where n is the given number.
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

    return sorted(set(divisors_list))