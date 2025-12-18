"""
QUESTION:
Write a function `remove_duplicates(lst)` that takes a list `lst` as input, removes duplicates while maintaining the original order of elements, and uses only a single loop. The function should return a new list containing only the unique elements.
"""

def remove_duplicates(lst):
    unique_elements = []
    seen_elements = set()
    
    for element in lst:
        if element not in seen_elements:
            seen_elements.add(element)
            unique_elements.append(element)
    
    return unique_elements