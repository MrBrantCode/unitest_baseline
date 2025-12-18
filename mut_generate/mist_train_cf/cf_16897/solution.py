"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input, sorts the positive integers in ascending order and negative integers in descending order, and returns the sorted array. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def custom_sort(arr):
    positive = sorted([num for num in arr if num > 0])
    negative = sorted([num for num in arr if num < 0], reverse=True)
    combined = negative + positive
    return combined