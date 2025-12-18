"""
QUESTION:
Create a function `calculate_result(C, V, nums)` that takes in three NumPy arrays: `C`, `V`, and `nums`, and returns the result of the element-wise multiplication of `C` and `V` divided element-wise by `nums`. The array `C` should be broadcasted to match the shape of `V`. The function should return the resulting NumPy array.
"""

import numpy as np

def entance(C, V, nums):
    result = (C * V) / nums
    return result