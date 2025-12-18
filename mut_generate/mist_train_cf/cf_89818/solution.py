"""
QUESTION:
Implement a function named `delete_element` that takes a multi-dimensional array `arr` and an `element` as input. The function should recursively delete all occurrences of the `element` from the `arr` without using any built-in array methods or data structures. The function should return the modified multi-dimensional array. The `arr` can have nested arrays of arbitrary depth and may contain non-array elements that should be preserved.
"""

def delete_element(arr, element):
    if not isinstance(arr, list):
        return None
    
    new_arr = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            nested_arr = delete_element(arr[i], element)
            if nested_arr is not None:
                new_arr.append(nested_arr)
        elif arr[i] != element:
            new_arr.append(arr[i])
    
    return new_arr if new_arr else None