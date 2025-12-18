"""
QUESTION:
Create a function `shift_array(arr, k)` that takes an array `arr` and a positive integer `k` as parameters. The function should return a new array where the elements of the original array are shifted `k` positions to the right, wrapping around to the beginning of the array if `k` is greater than the length of the array.
"""

def shift_array(arr, k):
    effective_shift = k % len(arr)
    shifted_array = []
    for i in range(len(arr)):
        new_index = (i + effective_shift) % len(arr)
        shifted_array.insert(new_index, arr[i])
    return shifted_array