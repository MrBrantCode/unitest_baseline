"""
QUESTION:
Design a function `rotate_array(arr, k)` that rotates the elements of array `arr` to the right by `k` steps. The function should handle cases where `k` is greater than the length of `arr` and return the rotated array. Note that a rotation of `0` or a multiple of the length of `arr` should return the original array.
"""

def rotate_array(arr, k):
    # Calculating the effective rotation - essential for when k is larger than len(arr)
    k = k % len(arr)

    # Check if rotation is necessary
    if k == 0:
        return arr

    # Perform rotation
    return arr[-k:] + arr[:-k]