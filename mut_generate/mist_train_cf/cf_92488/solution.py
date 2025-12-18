"""
QUESTION:
Write a function `is_perfect_number` that takes a positive integer `num` as input and returns a boolean value indicating whether the number is perfect or not. A number is said to be perfect if the sum of its proper divisors (all divisors excluding the number itself) is equal to itself. The input number will not exceed 10^6.
"""

import math

def is_perfect_number(num):
    if num <= 1:
        return False
    
    divisors_sum = 1
    sqrt_num = int(math.sqrt(num))
    
    for i in range(2, sqrt_num+1):
        if num % i == 0:
            divisors_sum += i
            quotient = num // i
            if quotient != i:
                divisors_sum += quotient
    
    return divisors_sum == num