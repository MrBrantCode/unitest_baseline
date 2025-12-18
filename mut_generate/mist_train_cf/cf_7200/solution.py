"""
QUESTION:
Write a function called `delete_element` that takes in a multi-dimensional array `arr` and an element `element`. The function should delete all occurrences of `element` from `arr` without using any built-in array methods or data structures. The function should also handle non-array elements and remove them if they match the element to be removed. The function should handle edge cases where `arr` is empty or contains only non-array elements.
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
    
    return new_arr