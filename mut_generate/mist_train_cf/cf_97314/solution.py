"""
QUESTION:
Create a function named `concatenate_arrays` that takes two arrays `arr1` and `arr2` as input and returns a new array that is the concatenation of `arr1` and `arr2` with no duplicate elements. The function cannot use built-in array concatenation methods or functions.
"""

def concatenate_arrays(arr1, arr2):
    result = []
    seen = set()

    for num in arr1:
        if num not in seen:
            result.append(num)
            seen.add(num)

    for num in arr2:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result