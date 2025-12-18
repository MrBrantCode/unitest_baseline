"""
QUESTION:
Write a function called `remove_duplicates` that takes a non-empty array of integers as input and returns a new array with duplicates removed, maintaining the original order of elements. The function should not use any built-in functions or data structures (such as sets or hashmaps) and should perform the operation in-place without allocating extra space or using additional data structures.
"""

def remove_duplicates(arr):
    arr.sort()
    next_non_duplicate = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
    return arr[:next_non_duplicate]