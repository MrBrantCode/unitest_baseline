"""
QUESTION:
Write a function `is_perfect_number` that takes a positive integer `num` as its parameter and returns a boolean value indicating whether `num` is a perfect number or not. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
"""

def is_perfect_number(num):
    if num <= 0:
        return False  

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num