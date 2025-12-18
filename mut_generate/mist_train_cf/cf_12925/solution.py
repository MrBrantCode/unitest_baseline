"""
QUESTION:
Write a function `remove_duplicates(arr)` that removes duplicates from the input array `arr` and returns a sorted array of unique values in ascending order. The function should use O(1) additional space and have a time complexity of O(n), where n is the length of the input array. The input array can contain integers, floating-point numbers, and strings.
"""

def remove_duplicates(arr):
    arr.sort()
    current = 0
    next_unique = 1
    while next_unique < len(arr):
        if arr[current] != arr[next_unique]:
            current += 1
            arr[current] = arr[next_unique]
        next_unique += 1
    return arr[:current+1]