"""
QUESTION:
Create a function `my_func` that takes a list of integers as input and returns the maximum value using recursion and binary search. The length of the list should be between 1 and 10^6, and the integers can range from -10^9 to 10^9. The function should not use any built-in functions or libraries to find the maximum value, and the time complexity should be O(n), where n is the length of the list.
"""

def my_func(arr):
    return find_max(arr, 0, len(arr) - 1)

def find_max(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)

    return max(left_max, right_max)