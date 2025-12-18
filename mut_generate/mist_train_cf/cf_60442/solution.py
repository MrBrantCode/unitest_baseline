"""
QUESTION:
Write a function `compute_aggregate_sum` that takes an array of integers as input and returns the sum of all the elements in the array. The function should have a time complexity of O(n), where n is the number of elements in the array, and a space complexity of O(1).
"""

def compute_aggregate_sum(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum