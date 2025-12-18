"""
QUESTION:
Write a function called `smallest_triang_num` that takes an integer `n` as input and returns a tuple containing the index and value of the smallest triangular number with `n` digits. The function should use the mathematical formula to calculate the index and triangular number.
"""

import math

def smallest_triang_num(n):
    index = math.ceil((math.sqrt((8 * math.pow(10,(n-1))) + 1) -1) / 2)
    triang_num = (index * (index + 1))//2
    return index, triang_num