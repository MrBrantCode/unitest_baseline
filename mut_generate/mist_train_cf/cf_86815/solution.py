"""
QUESTION:
Create a function `get_unique_elements(lst)` that takes a list `lst` as input, returns a new list containing only the unique elements from the original list in their original order, and modifies the original list to contain only unique elements. The function should be able to handle lists containing any hashable elements and should optimize for large datasets.
"""

def get_unique_elements(lst):
    unique_elements = []
    seen = set()
    
    for element in lst:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    
    lst.clear()
    lst.extend(unique_elements)
    
    return unique_elements