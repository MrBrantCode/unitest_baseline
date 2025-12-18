"""
QUESTION:
Write a function `is_perfect_number(num)` that checks if a given positive integer `num` is a perfect number. A number is perfect if the sum of its proper divisors is equal to itself. The function should return a boolean value indicating whether the number is perfect or not. The input number will not exceed 10^12 and the solution should have a time complexity of O(sqrt(n)), where n is the input number.
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
            if i != num // i:
                divisors_sum += num // i
    
    return divisors_sum == num