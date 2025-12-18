"""
QUESTION:
Create a function named `is_sorted` that determines whether a given array is sorted in either ascending or descending order. The function should have a time complexity of O(n), where n is the number of elements in the array, and should return `True` if the array is sorted in the given order and `False` otherwise.
"""

def is_sorted(array):
    order = None
    for i in range(1, len(array)):
        if order is None:
            if array[i] > array[i-1]:
                order = "ascending"
            elif array[i] < array[i-1]:
                order = "descending"
        if (order == "ascending" and array[i] < array[i-1]) or (order == "descending" and array[i] > array[i-1]):
            return False
    return True