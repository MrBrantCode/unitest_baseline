"""
QUESTION:
Write a function named `has_duplicate` that takes an array of integers as input and returns `True` if the array has duplicate elements and `False` otherwise. The array contains integer elements ranging from 1 to 1000. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def has_duplicate(arr):
    # Create a set to store unique elements
    unique_elements = set()

    for num in arr:
        # If the element is already present in the set, it's a duplicate
        if num in unique_elements:
            return True

        # Add the element to the set
        unique_elements.add(num)

    # No duplicates found
    return False