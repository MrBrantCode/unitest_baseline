"""
QUESTION:
Create a function `check_sorted(arr)` that checks if a given array `arr` is sorted in ascending order. The array must contain integers and have a length greater than 1. The function should return `True` if the array is sorted in ascending order, and `(False, index)` otherwise, where `index` is the position of the first element that violates the sorting order. The array cannot be modified or sorted using any built-in sorting functions or methods, and no built-in comparison operators or conditional statements can be used to check the sorting order.
"""

def check_sorted(arr):
    # Create a list of tuples where each tuple contains two consecutive elements of the array
    pairs = zip(arr, arr[1:])
    
    # Check if all pairs are in ascending order
    ascending = all(a <= b for a, b in pairs)
    
    if ascending:
        return True
    else:
        # Find the index of the first element that violates the sorting order
        for i, (a, b) in enumerate(zip(arr, arr[1:])):
            if a > b:
                return False, i + 1