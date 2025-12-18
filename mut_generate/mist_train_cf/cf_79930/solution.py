"""
QUESTION:
Create a function called `is_strictly_ascending` that takes a list of integers as input and returns `True` if the list is strictly ascending (i.e., each element is greater than the previous one) and `False` otherwise. The function should only consider the input list and not any external information.
"""

def is_strictly_ascending(arr):
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return False
    return True

def is_strictly_ascending(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1))