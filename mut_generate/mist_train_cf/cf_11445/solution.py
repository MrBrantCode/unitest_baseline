"""
QUESTION:
Create a function named `contains_duplicate` that takes a list `lst` as input. The function should return `True` if the list contains at least one duplicate element and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input list `lst`.
"""

def contains_duplicate(lst):
    unique_elements = set()
    for num in lst:
        if num in unique_elements:
            return True
        unique_elements.add(num)
    return False