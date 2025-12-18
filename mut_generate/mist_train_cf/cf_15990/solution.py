"""
QUESTION:
Write a function `sum_of_absolute_values` that takes two integers `a` and `b` as input and returns the sum of their absolute values. If the sum exceeds 10, the function should return the sum multiplied by 2.
"""

def sum_of_absolute_values(a, b):
    sum_of_values = abs(a) + abs(b)
    
    if sum_of_values > 10:
        return sum_of_values * 2
    else:
        return sum_of_values