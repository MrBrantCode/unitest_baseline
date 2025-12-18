"""
QUESTION:
Create a function `common_elements_frequency(list1, list2)` that takes two lists of integers as input and returns a dictionary where keys are the common elements of the two lists and their corresponding values are the minimum frequency of occurrence of the common elements in the two lists. The keys in the returned dictionary should maintain the same order as in the first list. The function should achieve this in a time complexity of O(n).
"""

from typing import Dict, List

def common_elements_frequency(list1: List[int], list2: List[int]) -> Dict[int, int]:
    list2_frequency = {}
    common_elements = {}

    # Build the frequency dictionary for the second list
    for num in list2:
        if num in list2_frequency:
            list2_frequency[num] += 1
        else:
            list2_frequency[num] = 1

    # Check for common elements and their frequency
    for num in list1:
        if num in list2_frequency and num not in common_elements:
            common_elements[num] = list2_frequency[num]

    return common_elements