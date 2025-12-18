"""
QUESTION:
Write a function named `compute_difference` that takes a list of integers as input and returns the difference between the highest and lowest values in the list. The function should handle empty lists, duplicate values, and negative numbers, and should have a time complexity of O(n) and a space complexity of O(1).
"""

def compute_difference(arr):
    if len(arr) == 0:
        return 0
    min_val = max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val - min_val