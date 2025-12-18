"""
QUESTION:
Create a function `containsDuplicates(arr)` that takes an array of integers as input and returns `True` if the array does not contain duplicates and `False` otherwise. The function should have a time complexity of O(n) or less and a space complexity of O(n) or less.
"""

def containsDuplicates(arr):
    unique_set = set()
    for num in arr:
        if num in unique_set:
            return False
        unique_set.add(num)
    return True