"""
QUESTION:
Create a function `common_elements(list1, list2)` that takes two lists of integers as input and returns a list of integers that appear in both `list1` and `list2`, maintaining the order of elements from `list1`. The function should also handle duplicate elements and achieve this in O(n) time complexity.
"""

from typing import List

def common_elements(list1: List[int], list2: List[int]) -> List[int]:
    count1 = {}
    for number in list1:
        if number in count1:
            count1[number] += 1
        else:
            count1[number] = 1
    
    count2 = {}
    for number in list2:
        if number in count2:
            count2[number] += 1
        else:
            count2[number] = 1
    
    result = []
    for number in list1:
        if number in count2 and count1[number] > 0 and count2[number] > 0:
            result.append(number)
            count1[number] -= 1
            count2[number] -= 1
    
    return result