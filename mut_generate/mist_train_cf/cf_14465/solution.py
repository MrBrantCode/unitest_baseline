"""
QUESTION:
Create a function named `remove_duplicates` that takes a list `lst` as an argument and returns a new list containing the unique elements from `lst` in the original order. The function should use only a single loop and not use any built-in Python functions that remove duplicates (e.g., set conversion or list comprehension with if conditions that use sets).
"""

def remove_duplicates(lst):
    unique_elements = []
    seen_elements = set()
    
    for element in lst:
        if element not in seen_elements:
            seen_elements.add(element)
            unique_elements.append(element)
    
    return unique_elements