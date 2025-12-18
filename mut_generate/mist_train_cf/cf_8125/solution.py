"""
QUESTION:
Create a function `rotate_array(arr, k)` that rotates the input array `arr` to the right by `k` steps. The function should take an array `arr` and a positive integer `k` as input, and return the rotated array. The function should have a time complexity of O(n), where `n` is the length of the array. The function should handle cases where `k` is larger than the length of the array.
"""

def rotate_array(arr, k):
    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)
    k = k % n
    reverse_array(0, n-1)
    reverse_array(0, k-1)
    reverse_array(k, n-1)
    return arr