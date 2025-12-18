"""
QUESTION:
Create a function named `smoothclamp` that takes in three parameters: `x`, `min_val`, and `max_val`. This function should behave similarly to the clamp function, but with a continuous derivative. The function should return `min_val` if `x` is less than `min_val`, `max_val` if `x` is greater than `max_val`, and a smoothly interpolated value between `min_val` and `max_val` otherwise.
"""

def smoothclamp(x, min_val, max_val):
    t = (x-min_val) / (max_val-min_val) # Normalize x to range[0, 1]
    t = max(0, min(1, t)) # Clamp t in [0, 1]
    t = t*t*(3 - 2*t) # Smooth t
    return t * (max_val - min_val) + min_val # Scale and shift to original range