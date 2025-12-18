"""
QUESTION:
Create a function named `find_largest_element` that takes a list of integers as input and returns a tuple containing the largest element and its first occurrence index. If the list is empty, return -1. The function should have a time complexity of O(n) and a space complexity of O(1), without using any built-in functions or libraries that directly solve the problem.
"""

def find_largest_element(arr):
    if len(arr) == 0:
        return -1
    largest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return largest, index