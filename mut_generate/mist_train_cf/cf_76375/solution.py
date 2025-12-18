"""
QUESTION:
Write a function named `process` that takes a two-dimensional array as input and inverts the elements within each subarray without using any built-in reverse functions or array methods. The function should handle nested arrays within the two-dimensional array and edge cases such as empty or undefined values. The function should be efficient in terms of speed and memory management.
"""

def process(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            arr[i] = process(arr[i])
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr