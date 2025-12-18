"""
QUESTION:
Create a function called `rolling_max` that takes two lists of integers, `numbers1` and `numbers2`, as input. The function should return two lists where each element at index `i` is the maximum value found so far in the corresponding input list up to and including index `i`. The function should return these two lists as a tuple. The function should assume that the input lists are of equal length and that both lists have at least one element.
"""

from typing import List, Tuple

def rolling_max(numbers1: List[int], numbers2: List[int]) -> Tuple[List[int], List[int]]:
    max_nums1 = [numbers1[0]]
    max_nums2 = [numbers2[0]]
    
    for i in range(1, len(numbers1)):
        max_nums1.append(max(max_nums1[-1], numbers1[i]))
        max_nums2.append(max(max_nums2[-1], numbers2[i]))
        
    return (max_nums1, max_nums2)