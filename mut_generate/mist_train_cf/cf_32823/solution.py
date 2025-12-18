"""
QUESTION:
Implement a function `find_min_state_size(x, k, window_size)` that takes in three parameters: 
- `x`: a list of numerical values, 
- `k`: a positive integer, 
- `window_size`: a positive integer.

The function should calculate the minimum standard deviation of subarrays of `x` with size `window_size`, then multiply it by `k`, and return the result. If `x` is empty or cannot form a subarray of size `window_size`, return 0.
"""

import numpy as np

def find_min_state_size(x, k, window_size):
    sos_temp = []
    for i in range(1 + len(x) - window_size):
        subarray = x[i : i + window_size]
        std_dev = np.std(subarray, ddof=1)
        sos_temp.append(std_dev)
    if not sos_temp:
        return 0
    else:
        return min(sos_temp) * k