"""
QUESTION:
Write a function named `find_smallest` that takes an array of numbers as input and returns the smallest number in the array. The function should not use the built-in `min()` function or any other built-in functions that find the minimum value. The function should have a time complexity of O(n), where n is the size of the array, and use constant space complexity.
"""

def find_smallest(arr):
    if len(arr) == 0:
        return None

    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num

    return smallest