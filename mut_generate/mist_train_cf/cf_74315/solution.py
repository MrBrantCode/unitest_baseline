"""
QUESTION:
Write a function `advanced_geometric_mean_in_range` that takes a list of integers `l`, a minimum value `min_val`, and a maximum value `max_val` as input. The function should return `True` if the geometric mean of the absolute values of the integers in `l` falls within the range `[min_val, max_val]`, and `False` otherwise. The function should also return `False` if the list is empty, contains zero, or contains negative numbers.
"""

from typing import List
import math

def advanced_geometric_mean_in_range(l: List[int], min_val: int, max_val: int) -> bool:
    if len(l) == 0:
        return False
    elif 0 in l:
        return False
    elif any(i < 0 for i in l):
        return False
    else:
        geometric_mean = math.prod([(abs(x))**(1.0/len(l)) for x in l])
        return min_val <= geometric_mean <= max_val