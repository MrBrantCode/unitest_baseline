"""
QUESTION:
Write a function named `count_occurrences` that takes three parameters: `lst` (a list that may contain elements of various data types, including integers, strings, dictionaries, and sublists), `element`, and `data_type`. The function should count the occurrences of `element` in `lst` while ignoring any occurrences within nested sublists and considering only elements of type `data_type`. Return the total count of occurrences of `element` in `lst` that match the specified `data_type`.
"""

def count_occurrences(lst, element, data_type):
    count = 0
    
    def count_element(lst):
        nonlocal count
        
        for item in lst:
            if isinstance(item, list):
                continue  # Ignore occurrences within nested sublists
            elif isinstance(item, data_type) and item == element:
                count += 1
    
    count_element(lst)
    return count