"""
QUESTION:
Write a function `calculate_sum_recursive` that takes three parameters: `num`, `limit`, and `exclude`, to calculate the sum of the numbers from `num` to `limit`, excluding any numbers divisible by both 5 and 7. The function should use recursion instead of a loop. The function should return the calculated sum.
"""

def calculate_sum_recursive(num, limit, exclude):
    if num > limit:
        return 0
    elif num % 5 == 0 and num % 7 == 0:
        return calculate_sum_recursive(num+1, limit, exclude)
    else:
        return num + calculate_sum_recursive(num+1, limit, exclude)