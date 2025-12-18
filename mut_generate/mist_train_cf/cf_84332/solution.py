"""
QUESTION:
Create a function named `reorder_descendant` that takes an array as input, creates a copy of the array to avoid modifying the original, and returns the copied array sorted in descending order without using any built-in sorting methods. The array can contain any number of elements, and all elements are integers. The function should have a time complexity of O(n^2) or better.
"""

def reorder_descendant(array):
    array_copy = array.copy()  # create a copy to not modify the original array
    length = len(array_copy)

    for i in range(length):
        for j in range(0, length-i-1):
            if array_copy[j] < array_copy[j+1]:  # compare elements and swap if needed
                array_copy[j], array_copy[j+1] = array_copy[j+1], array_copy[j]
    return array_copy