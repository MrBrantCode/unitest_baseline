"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of strings and a target integer as input, where each string in the list is in the format 'abc*def' with 'abc' and 'def' as integers. The function should parse integers from the strings, perform a binary search, and return `True` if the target integer is found and `False` otherwise. The function should handle edge cases such as an empty list or a list with one element.

The input list is sorted based on the first integer in each string. If two strings have the same first integer, they are sorted based on the second integer. The function should be optimized for time and space complexity.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        vals = [int(val) for sublist in [x.split('*') for x in arr[mid].split()] for val in sublist]
        for val in vals:
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
    return False