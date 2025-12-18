"""
QUESTION:
Create a function named `is_unique_array` that takes an array of elements as input and returns True if all elements in the array are unique, and False otherwise. The function must have a time complexity of O(n), where n is the length of the array.
"""

def is_unique_array(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return False
        seen.add(num)
    return True