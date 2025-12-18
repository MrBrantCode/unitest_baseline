"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of elements as input and returns a new list with duplicate elements removed, preserving the original order of elements. The function should handle a list of any comparable elements (e.g., integers, strings).
"""

def remove_duplicates(objects):
    new_list = []
    for obj in objects:
        if obj not in new_list:
            new_list.append(obj)
    return new_list