"""
QUESTION:
Write a function `is_irrational(n: float)` that takes a real number `n` as input and returns `True` if `n` is an irrational number, and `False` otherwise. The function should work for all real number inputs and efficiently detect if `n` is rational or irrational. Note that due to the limitations of floating point representation in Python, the function may not work as expected with mathematically-defined irrational numbers.
"""

import math

def is_irrational(n: float):
    # check whether the number is negative, if negative return False
    if n<0:
        return False
     
    # calculate the square root of the number
    root = math.isqrt(n)
    
    # if the square root squared does not return the original number
    # it means that the number is an irrational number
    if root * root != n:
        return True
    # if the square root squared returns the original number
    # it means that the number is a rational number
    return False