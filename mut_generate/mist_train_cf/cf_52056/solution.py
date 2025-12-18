"""
QUESTION:
Create a function called `has_duplicates` that takes an array of elements as input and returns `True` if there are any duplicate elements in the array, and `False` otherwise. The function should have a time complexity of O(n).
"""

def has_duplicates(arr):
    found = set()
    for a in arr:
        if a in found:
            return True
        found.add(a)
    return False