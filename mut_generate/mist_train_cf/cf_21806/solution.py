"""
QUESTION:
Create a function `clamp_number(num, min_val, max_val)` that takes a number `num` and a minimum value `min_val` and maximum value `max_val` as input. The function should return the clamped value of `num` between `min_val` and `max_val`, but with the following conditions: 
- If `num` is negative, use its absolute value instead.
- If the clamped value is within 10% of `min_val` or `max_val`, return a string describing the proximity to the boundary instead of the clamped value.
- The inputs can be floating-point numbers.
"""

def clamp_number(num, min_val, max_val):
    if num < 0:
        num = abs(num)
    
    if num < min_val:
        if min_val - num <= 0.1 * min_val:
            return f"The number is within 10% of the minimum value: {min_val - num} away from the boundary."
        else:
            return min_val
    elif num > max_val:
        if num - max_val <= 0.1 * max_val:
            return f"The number is within 10% of the maximum value: {num - max_val} away from the boundary."
        else:
            return max_val
    else:
        return num