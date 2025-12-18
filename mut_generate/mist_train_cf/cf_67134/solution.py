"""
QUESTION:
Implement a function `rearrange_two_elements(arr)` that determines whether it's possible to sort an array in non-decreasing order using the following steps: any number of right shift operations, and up to two swaps involving exactly two elements. The function should return `True` if it's possible to sort the array and `False` otherwise.
"""

def rearrange_two_elements(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                inversions += 1
    return inversions <= 2