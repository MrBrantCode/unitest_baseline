"""
QUESTION:
Write a function `find_intersection(list_a: List[int], list_b: List[int]) -> List[int]` that returns a list containing the intersection of two input lists, with no duplicates and where each element's frequency in the output list is the minimum of its frequency in the two input lists.
"""

from typing import List

def find_intersection(list_a: List[int], list_b: List[int]) -> List[int]:
    count_a = {}
    for num in list_a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1

    count_b = {}
    for num in list_b:
        if num in count_b:
            count_b[num] += 1
        else:
            count_b[num] = 1

    intersection = []
    for num in count_a.keys():
        if num in count_b:
            intersection.extend([num] * min(count_a[num], count_b[num]))
            
    return intersection