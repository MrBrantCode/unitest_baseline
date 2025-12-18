"""
QUESTION:
Write a function named `delete_elements_multi` that takes two parameters: a multi-dimensional array (`arr`) and a specific element (`element`). The function should delete all occurrences of the `element` from the `arr`, which can have nested arrays of arbitrary depth, without using any built-in array methods or data structures.
"""

def delete_elements_multi(arr, element):
    result = []
    for i in range(len(arr)):
        if type(arr[i]) == list:
            arr[i] = delete_elements_multi(arr[i], element)
        if arr[i] != element:
            result.append(arr[i])
    return result