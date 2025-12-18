"""
QUESTION:
Create a function named `LinearSearch` that takes two parameters: an unsorted array and a target item. Implement a linear search algorithm to find the index of the target item in the array. If the item is found, return its index; otherwise, return -1. The function should have a time complexity of O(n), where n is the length of the array, as it needs to potentially check every element in the array.
"""

def LinearSearch(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1