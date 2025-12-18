"""
QUESTION:
Create a function `check_duplicates(arr)` that takes a list of integers `arr` as input and returns a boolean value. The function should return `True` if the array contains any duplicate elements and `False` otherwise. However, it should immediately return `False` if the array has more than 100 elements or contains any negative integers. The input array is guaranteed to be sorted in ascending order.
"""

def check_duplicates(arr):
    # Check length of array
    if len(arr) > 100:
        return False

    # Check for negative integers
    if any(num < 0 for num in arr):
        return False

    # Check for duplicate elements
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True

    return False