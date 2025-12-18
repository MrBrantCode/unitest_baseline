"""
QUESTION:
Implement a function named `find_max` that takes an array `arr` and two integers `start` and `end` as input. The function should find the maximum value in the subarray `arr[start:end+1]` using a recursive approach with a time complexity of O(N) and space complexity of O(1), where N is the number of elements in the subarray.
"""

def find_max(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)

    return max(left_max, right_max)