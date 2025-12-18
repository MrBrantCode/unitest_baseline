"""
QUESTION:
Write a function `linear_search_max` that finds the maximum element in a given unsorted array using a linear search approach. The function should take one argument `arr`, which is a list of integers. The function should return the maximum element in the array.
"""

def find_maximum(arr):
    max_element = arr[0]
    for elem in arr[1:]:
        if elem > max_element:
            max_element = elem
    return max_element