"""
QUESTION:
Write a function named `find_max` that takes an unsorted list of integers as input and returns the maximum element using a linear search approach. The function should have a time complexity of O(N), where N is the number of elements in the list.
"""

def find_max(arr):
    max_element = arr[0]
    for i in arr:
        if i > max_element:
            max_element = i
    return max_element