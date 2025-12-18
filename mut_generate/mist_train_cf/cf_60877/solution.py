"""
QUESTION:
Create a function `sort_elements(arr)` that sorts the given array of alphanumeric elements in ascending order of their numerical and alphabetical values. The function should consider numerical values as the primary criteria and alphabetical values as the secondary criteria when there are numerical ties. If the array contains invalid entries, the function should report these cases as exceptions. The input array can contain alphanumeric strings with multiple digit-nondigit transition points, and variable order of digits and alphabets.

The function should be able to handle cases like "34ab12cd1" and should not assume that the string ends with an alphabet or that it contains at least one digit. It should also be able to handle cases where the string contains more than one character.

Create another function `binary_search(arr, x)` that performs a binary search on the sorted array to find the element `x`. If the element is found, the function should return its index; otherwise, it should return -1.
"""

import re

def sort_elements(arr):
    try:
        elements = [re.split('(\d+)', s) for s in arr]
        elements = [[int(i) if i.isdigit() else i for i in sublist if i] for sublist in elements]
        sorted_elements = sorted(elements, key=lambda x: [i for i in x if isinstance(i, int)] + [i for i in x if isinstance(i, str)])
        sorted_elements = [''.join(map(str, el)) for el in sorted_elements]
        return sorted_elements
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    arr = sort_elements(arr)
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1