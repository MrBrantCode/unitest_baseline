"""
QUESTION:
Write a function `find_max_sum_pair` that takes an array of integers as input and returns a pair of distinct elements with the maximum sum in the array. If multiple pairs have the same maximum sum, return the pair with the smallest first element. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def find_max_sum_pair(arr):
    arr.sort()
    return (arr[-2], arr[-1])