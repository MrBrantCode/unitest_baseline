"""
QUESTION:
Implement a function `custom_sort` that takes an array of integers `arr` as input and returns the array sorted in non-decreasing order using the selection sort algorithm. The function should work by iteratively finding the minimum value in the unsorted part of the array and swapping it with the first unsorted element. The function should have a time complexity of O(n^2) where n is the number of elements in the array.
"""

from typing import List

def custom_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr