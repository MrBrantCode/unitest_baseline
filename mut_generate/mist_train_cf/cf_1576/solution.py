"""
QUESTION:
Write a function `find_max_difference(arr)` that takes an array of integers as input and returns the pair of elements with the greatest difference, where the larger element is at an index greater than the smaller element. If multiple pairs have the same maximum difference, return the pair with the smallest index of the smaller element. If there are no pairs that satisfy the condition, return an empty array. The function should have a time complexity of O(n).
"""

def find_max_difference(arr):
    min_element = float('inf')
    max_diff = 0
    min_idx = -1
    result = []

    for i in range(len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            min_idx = i

        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
            result = [min_element, arr[i]]

    return result