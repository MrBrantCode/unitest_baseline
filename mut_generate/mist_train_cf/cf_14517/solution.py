"""
QUESTION:
Create a function `max_value` that takes in three integer parameters `x`, `y`, and `z`. The function should return the maximum value among `x`, `y`, and `z`. If the maximum value is negative, the function should return its absolute value. If all three parameters are zero, the function should return zero.
"""

def max_value(x, y, z):
    max_val = max(x, y, z)
    if max_val < 0:
        return abs(max_val)
    elif max_val == 0:
        return 0
    else:
        return max_val