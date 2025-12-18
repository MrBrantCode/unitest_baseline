"""
QUESTION:
Write a function `second_smallest(arr)` that takes an array of integers as input and returns the second smallest unique element in the array. If the array has less than two unique elements, the function should return `None`. The function should be efficient and handle duplicate elements.
"""

def second_smallest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[1] if len(arr) > 1 else None