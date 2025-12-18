"""
QUESTION:
Given a list of integers (1 <= integers <= 10^9) with a maximum of 10^6 elements, write a function `find_odd_occurrence(arr)` that returns the integer that appears an odd number of times in the list. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result