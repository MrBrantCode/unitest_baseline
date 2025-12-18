"""
QUESTION:
Given an integer array 'arr' and a limit on unique element modifications, determine the least number of elements that need to be altered to convert the array into a palindrome, where a single element can be altered to any other element in one operation. If the number of required changes exceeds the given limit, return -1. The function should be named `minimum_changes_to_palindrome` and take two parameters: `arr` (the input array) and `limit` (the maximum allowed modifications).
"""

def minimum_changes_to_palindrome(arr, limit):
    changes = 0
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            changes += 1
        if changes > limit:
            return -1
    return changes