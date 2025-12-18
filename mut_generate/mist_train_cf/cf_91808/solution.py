"""
QUESTION:
Write a function named `find_unique_items` that takes a list as input and returns a list of unique items from the input list. The function should not use any built-in functions or data structures. The function should implement its own logic to find and remove duplicate items.
"""

def find_unique_items(lst):
    result = []
    
    for item in lst:
        is_unique = True
        
        for unique_item in result:
            if item == unique_item:
                is_unique = False
                break
        
        if is_unique:
            result.append(item)
    
    return result