"""
QUESTION:
Write a function `rolling_max` that takes two lists of integers `numbers1` and `numbers2` as input and returns a tuple of two lists. Each output list contains the rolling maximum of the corresponding input list, i.e., for the i-th element in the list, the rolling maximum would be the maximum of all elements in the list up to i. The two input lists are guaranteed to be non-empty and of the same length.
"""

from typing import List, Tuple

def rolling_max(numbers1: List[int], numbers2: List[int]) -> Tuple[List[int], List[int]]:
    max1, max2 = [], []
    running_max1, running_max2 = numbers1[0], numbers2[0]
    
    for num1, num2 in zip(numbers1, numbers2):
        running_max1 = max(running_max1, num1)
        running_max2 = max(running_max2, num2)
        max1.append(running_max1)
        max2.append(running_max2)
    
    return max1, max2