"""
QUESTION:
Write a function `has_duplicates` that takes a list of integers as input and returns `True` if the list has duplicate elements and `False` otherwise. The function should have a time complexity of O(n log n) and a space complexity of O(n), and it should be able to handle lists containing integers ranging from 1 to 10^6.
"""

def has_duplicates(arr):
    arr.sort()  # Sort the array in O(n log n) time complexity
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:  # Check if there are adjacent elements that are equal
            return True
    return False