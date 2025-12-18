"""
QUESTION:
Create a function `divisible_by_all(num, divisor_list)` that takes a number `num` and a list of integers `divisor_list` as input. The function should return `True` if `num` can be divided evenly by every integer in `divisor_list` and also by 5, and `False` otherwise.
"""

def divisible_by_all(num, divisor_list):
    for divisor in divisor_list:
        if num % divisor != 0:
            return False
    return num % 5 == 0