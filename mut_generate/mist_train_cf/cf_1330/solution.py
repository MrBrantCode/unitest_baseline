"""
QUESTION:
Given an array of integers, find the index of the element that appears an odd number of times. The function should be implemented as `find_odd_occurrence(arr)` where `arr` is the input array. The array will contain at most 10^6 elements and each element will be an integer between -10^9 and 10^9 (inclusive). The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num

    for i, num in enumerate(arr):
        if num == result:
            return i