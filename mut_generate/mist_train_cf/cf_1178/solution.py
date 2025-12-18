"""
QUESTION:
Write a function `get_unique_elements` that takes a list of elements as input and returns a new list containing only the unique elements from the original list, while preserving the order. The function should be able to handle lists containing various data types, including integers, strings, and floats, and should be optimized for large datasets.
"""

def get_unique_elements(lst):
    unique_elements = []
    seen = set()
    
    for element in lst:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    
    return unique_elements