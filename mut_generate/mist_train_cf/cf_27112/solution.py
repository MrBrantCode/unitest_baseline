"""
QUESTION:
Implement a function called `nested_if_else` that takes a NumPy array `x` as input. The function should modify the array elements based on the following conditions:
- If the element is greater than 0.5, set it to 1.
- If the element is less than -0.5, set it to -1.
- If the element is between -0.5 and 0.5 (inclusive), set it to 0.
The function should return the modified array.
"""

import numpy as np

def nested_if_else(x):
    x[x > 0.5] = 1
    x[x < -0.5] = -1
    x[(x >= -0.5) & (x <= 0.5)] = 0
    return x