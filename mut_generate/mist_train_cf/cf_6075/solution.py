"""
QUESTION:
Implement a recursive function `log_base_10` to find the logarithm (base 10) of a number without using any built-in logarithm functions or libraries. The function should take two parameters: `num` (the input number) and the initial `low` and `high` values for the search space. If `num` is less than or equal to 0, the function should return `float('nan')` or `float('-inf')` as the logarithm is undefined for non-positive numbers.
"""

def log_base_10(num, low, high):
    if num == 0:
        return float('-inf')  # log(0) is undefined
    elif num == 1:
        return 0  # log(1) is 0
    elif num < 0:
        return float('nan')  # log of negative number is undefined
    
    mid = (low + high) // 2

    if mid == low:
        return mid

    if 10**mid == num:
        return mid
    elif 10**mid < num:
        return log_base_10(num, mid, high)
    else:
        return log_base_10(num, low, mid)