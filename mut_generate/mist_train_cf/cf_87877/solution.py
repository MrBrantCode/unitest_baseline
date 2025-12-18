"""
QUESTION:
Write a function named `same_orientation` that takes an array of integers or floating point numbers as input and returns `True` if all non-zero elements in the array are similarly oriented (i.e., either all positive or all negative), and `False` otherwise. If the array contains only zero values or is empty, the function should return `True`. The function should have a time complexity of O(n), where n is the length of the input array, and should not use any built-in functions that directly solve the problem.
"""

def same_orientation(arr):
    if len(arr) <= 1:
        return True
    elif arr[0] == 0:
        return all(x == 0 for x in arr)
    else:
        orientation = arr[0] > 0
        for num in arr:
            if (num > 0) != orientation and num != 0:
                return False
        return True