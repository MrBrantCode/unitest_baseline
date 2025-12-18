"""
QUESTION:
Create a function named `create_new_array` that takes an array of integers as input, removes negative numbers and duplicates, and returns the resulting array in ascending order. The function should have a time complexity of O(n log n) or better.
"""

def create_new_array(arr):
    positive_nums = set()
    for num in arr:
        if num > 0:
            positive_nums.add(num)
    return sorted(positive_nums)