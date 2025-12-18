"""
QUESTION:
Implement the function `calc_C(n)` that takes an integer `n` as input and returns the number of cuboids that contain `n` cubes in one of its layers. The function should calculate this value based on the given formula: `n = 4(a+b+c) - 12`, where `a`, `b`, and `c` are the dimensions of the cuboid with `a >= b >= c >= 1` and `a, b, c` are integers.

Restrictions: `n` is an even number and `a, b, c` are positive integers.
"""

import numpy as np

def calc_C(n):
    """
    Calculate the number of cuboids that contain n cubes in one of its layers.
    
    Parameters:
    n (int): The number of cubes in one layer of the cuboid.
    
    Returns:
    int: The number of cuboids that contain n cubes in one of its layers.
    """
    counter = np.zeros((200000), dtype=int)
    limit = (n + 12) // 4
    for c in range(1, limit + 1):
        max_b = min(c, limit - c + 1)
        for b in range(c, max_b + 1):
            max_a = min(b, ((n + 12) - 4 * (b + c)) // 2 )
            min_a = (n + 12 - 4 * (b + c - 1)) // 4
            counter[n] += max(0, max_a - min_a + 1) 
    return counter[n]