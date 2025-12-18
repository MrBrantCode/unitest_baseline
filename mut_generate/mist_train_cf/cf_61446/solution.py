"""
QUESTION:
Implement a function named `isSorted` in Python that checks whether a given array (including nested arrays) is sorted, and if so, determines the type of sorting (ascending or descending). The function should handle arrays with complex nested structures and up to one million numbers. If the array contains equal adjacent elements, the function should indicate uncertainty in determining the type of sorting. The function should return a string message stating whether the array is sorted, the type of sorting, or if it's not possible to determine the type of sorting with certainty.

Constraints:
- Nested arrays should be considered in sequence with the rest of the main array.
- The array may contain up to one million positive or negative integers within the system's integer limit.
- The implementation should be optimized for performance to handle large arrays within a reasonable timeframe.
"""

def isSorted(array):
    # Define a function to flatten nested array
    def flatten(array, flat=None):
        if flat is None:
            flat = []

        for el in array:
            if isinstance(el, list):
                flatten(el, flat)
            else:
                flat.append(el)

        return flat

    # Flatten array
    array = flatten(array)

    n = len(array)
    
    if n == 1 or n == 0:
        return "Array is sorted (ascending)"
    elif n == 2 and array[0] == array[1]:
        return "Array is sorted but adjacent elements are equal"

    flag = None  # flag = 1 if sorted ascending, flag = -1 if sorted descending
    for i in range(n - 1):
        if array[i] == array[i + 1]:
            if flag is not None: 
                continue
        elif array[i] < array[i + 1]:
            if flag is not None and flag != 1:
                return "Array is not sorted"
            elif flag is None:
                flag = 1
        else:
            if flag is not None and flag != -1:
                return "Array is not sorted"
            elif flag is None:
                flag = -1

    if flag == 1:
        return "Array is sorted (ascending)"
    elif flag == -1:
        return "Array is sorted (descending)"
    else:
        return "Array is sorted but adjacent elements are equal"