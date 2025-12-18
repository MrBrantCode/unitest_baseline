"""
QUESTION:
Write a function named `count_L_values` that takes a positive integer `max_distance` and an integer `B` as input, and returns the quantity of values of `L` that are less than or equal to `max_distance` for which `B(L) = B`. The `B(L)` function is defined as the number of cells in a hexagonal honeycomb that are at a distance `L` from the center cell, where distances are measured from the center of one cell to the center of another, and `B(L) = m * 6` for some positive integer `m`. The distance `L` is related to `m` by the equation `L = sqrt(3 * m^2 - 3 * m + 1)`.
"""

import math

def count_L_values(max_distance, B):
    count = 0
    m = B // 6
    for i in range(m - 1, m + 2):  
      L = math.sqrt(3 * math.pow(i, 2) - 3 * i + 1)
      count += 1 if L <= max_distance else 0
    return count