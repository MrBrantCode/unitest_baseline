"""
QUESTION:
Example

Input

100 1 0
50 100


Output

14.57738
"""

import math

def minimum_velocity_to_reach_target(d, n, b, O):
    def solve(b):
        l = d / (b + 1)
        idx = 0
        vx2 = 10 ** 9
        for i in range(b + 1):
            while idx < n and O[idx][0] * (b + 1) <= d * (i + 1):
                (p, h) = O[idx]
                p -= l * i
                vx2 = min(vx2, p * (l - p) / (2 * h))
                idx += 1
        if vx2 == 0:
            return 10 ** 9
        return l if l <= vx2 * 2 else vx2 + l ** 2 / (4 * vx2)
    
    return math.sqrt(min(map(solve, range(b + 1))))