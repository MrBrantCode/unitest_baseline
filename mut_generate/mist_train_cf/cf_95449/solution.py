"""
QUESTION:
Implement a function `remove_elements` that takes two array-like structures, `first` and `second`, and returns a new array containing all elements from `first` that do not appear in `second`. The function should handle arrays containing any type of element, including nested arrays, and recursively remove any elements that appear in `second`.
"""

def remove_elements(first, second):
    if not isinstance(first, (list, tuple)):  
        return first

    result = []
    for item in first:
        if isinstance(item, (list, tuple)):  
            item = remove_elements(item, second)

        if item not in second:
            result.append(item)

    return result