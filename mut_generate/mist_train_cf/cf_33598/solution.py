"""
QUESTION:
Create a function `is_perfect_number(num)` that takes a positive integer `num` as input and returns `True` if the number equals the sum of its proper divisors, excluding itself, and `False` otherwise.
"""

def entance(num):
    if num <= 0:
        return False  

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num