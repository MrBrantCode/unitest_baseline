"""
QUESTION:
Write a recursive function `recursive_calculation` that takes two parameters: `num` and `iteration`. The function should calculate `num + 2 - 2` and repeat this process for `10` iterations, returning the final result.
"""

def recursive_calculation(num, iteration):
    if iteration == 10:
        return num
    else:
        new_num = num + 2 - 2
        return recursive_calculation(new_num, iteration + 1)