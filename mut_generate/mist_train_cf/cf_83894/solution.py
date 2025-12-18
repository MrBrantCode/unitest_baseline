"""
QUESTION:
Define the function G(N) that returns the maximum number of lattice points in an axis-aligned N×N square that the graph of a single strictly concave decreasing function can pass through. The function G(N) should be calculated as follows: if N is a perfect square, G(N) = √N*2; otherwise, G(N) = (floor(√N)*2 + 1). Implement the function G(N) to calculate G(10^18).
"""

import math

def G(N):
    sqrt_N = math.sqrt(N)
    floor_sqrt_N = math.floor(sqrt_N)
    if sqrt_N == floor_sqrt_N:
        return floor_sqrt_N*2
    else:
        return floor_sqrt_N*2 + 1