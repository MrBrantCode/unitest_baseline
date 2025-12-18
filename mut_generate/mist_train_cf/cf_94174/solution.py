"""
QUESTION:
Find the index of the element that appears an odd number of times in an array of integers. The function should be named `find_odd_occurrence`. The array will contain at most 10^6 elements and each element will be an integer between 1 and 10^9 (inclusive). The time complexity of the solution should be O(n) and the space complexity should be O(1).
"""

def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result