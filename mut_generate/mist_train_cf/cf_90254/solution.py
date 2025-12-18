"""
QUESTION:
Create a function `rotate_array(arr, k)` that takes an array `arr` and a positive integer `k` as input, and returns the array rotated to the right by `k` steps. The function should have a time complexity of O(n), where n is the length of the array, and should be able to handle large arrays and large values of `k` efficiently.
"""

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse_array(0, n-1)
    reverse_array(0, k-1)
    reverse_array(k, n-1)

    return arr