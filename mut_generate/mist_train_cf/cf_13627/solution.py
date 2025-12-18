"""
QUESTION:
Implement a recursive function `find_max` that finds the maximum value in an array of integers, with a time complexity of O(N) and a space complexity of O(1). The function should take an array and the start and end indices of the subarray as input and return the maximum value in the subarray.
"""

def find_max(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)

    return max(left_max, right_max)