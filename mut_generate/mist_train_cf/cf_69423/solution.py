"""
QUESTION:
Create a function `advanced_sort` that takes a list of integers as input and returns the sorted list if it can be achieved by applying the following operations: 
1) reversing the order of any portion of the list, 
2) removing one or two elements from the list, 
3) swapping two elements a single time, and 
4) incrementing or decrementing one element by 1 only once. 
If the sorted list cannot be achieved, return the original list. The function should handle empty lists and return an empty list.
"""

from typing import List

def advanced_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []

    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:                                  # Rule 1
                arr[i], arr[j] = arr[j], arr[i]                  # Rule 3
            elif arr[i] == arr[j] and arr[i] + 1 < sorted_arr[i]: # Rule 4
                arr[i] += 1
            elif i > 0 and arr[i] < arr[i-1]:                     # Rule 1
                arr[i-1:i+1] = arr[i-1:i+1][::-1]                 # Rule 1
        if sorted_arr == arr:
            return sorted_arr
    if len(arr) > 2:                                             # Rule 2
        del arr[-1]
        return advanced_sort(arr)
    return arr