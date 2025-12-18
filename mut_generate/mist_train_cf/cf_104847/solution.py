"""
QUESTION:
Write a function called `has_duplicates` that takes an array `arr` as input and returns `True` if there are any duplicate elements in the array and `False` otherwise. The function should be implemented using a generator expression for efficiency.
"""

def has_duplicates(arr):
    return any(arr[i] == arr[j] for i in range(len(arr)) for j in range(i + 1, len(arr)))