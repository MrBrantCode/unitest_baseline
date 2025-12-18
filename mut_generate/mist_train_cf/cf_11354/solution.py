"""
QUESTION:
Create a function `find_unique_items(lst)` that takes a list `lst` as input and returns an array of unique items. The function should not use any built-in functions or data structures, such as sets or dictionaries, to solve the problem. The function should implement its own logic to find and remove duplicate items.
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