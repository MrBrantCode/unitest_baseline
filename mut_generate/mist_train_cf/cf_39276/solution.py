"""
QUESTION:
Implement the `sort_insertion` function to sort an array of integers in non-decreasing order using the insertion sort algorithm. The function should take a list of integers as input and return the sorted list.

The function should iterate through the input array starting from the second element, comparing each element with the elements in the sorted portion of the array and inserting it into the correct position. 

The function should return the sorted array.
"""

from typing import List

def sort_insertion(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr