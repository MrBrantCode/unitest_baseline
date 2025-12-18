"""
QUESTION:
Write a function `nested_list_summary(nested_list)` that takes a nested list of integers as input and returns a list of pairs, where each pair contains the first and last integer of each subarray in the input list. The function should be able to handle nested lists of arbitrary depth and ignore empty subarrays.
"""

from typing import List, Union

def nested_list_summary(nested_list: List[Union[int, List]]) -> List[List[int]]:
    def find_border(nest: List[Union[int, List]]) -> List[int]:
        if type(nest[0]) != list:
            first = nest[0]
        else:
            first = find_border(nest[0])[0]
        if type(nest[-1]) != list:
            last = nest[-1]
        else:
            last = find_border(nest[-1])[-1]
        return [first, last]

    result = []
    for sub_list in nested_list:
        if len(sub_list) > 0:  
            result.append(find_border(sub_list))
    return result