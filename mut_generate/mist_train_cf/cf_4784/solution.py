"""
QUESTION:
Write a function `create_new_array(arr)` that takes an array of integers as input, filters out the negative integers, sorts the remaining integers in ascending order, removes duplicates, and calculates the sum of the positive integers. The function should have a time complexity of O(n log n) or better.
"""

def create_new_array(arr):
    result = []
    for num in arr:
        if num > 0:
            result.append(num)
    result = sorted(set(result))
    positive_sum = sum(result)
    return result, positive_sum