"""
QUESTION:
Create a function called `remove_duplicates` that takes an array as input and returns the array with duplicates removed, while maintaining the highest frequency count of each element and preserving the original order.
"""

import collections

def remove_duplicates(arr):
    count = collections.Counter(arr)
    ordered_dict = collections.OrderedDict()
    
    for element in arr:
        if element in ordered_dict:
            ordered_dict[element] -= 1
            if ordered_dict[element] == 0:
                ordered_dict.pop(element)
        else:
            ordered_dict.setdefault(element, count[element])
    
    return list(ordered_dict.keys())