"""
QUESTION:
Implement a function `concatenate_arrays(arr1, arr2)` that concatenates two input arrays `arr1` and `arr2` and removes any duplicate elements from the resulting array without using any built-in array concatenation methods or functions. The function should return a new array containing all unique elements from both input arrays.
"""

def concatenate_arrays(arr1, arr2):
    result = []
    seen = set()

    # Add elements from arr1 to result
    for num in arr1:
        if num not in seen:
            result.append(num)
            seen.add(num)

    # Add elements from arr2 to result
    for num in arr2:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result