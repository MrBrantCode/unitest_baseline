"""
QUESTION:
Design a function `remove_duplicates` that removes duplicates from a nested list of arbitrary depth. The function should maintain the original order of elements and not use built-in functions for duplicate removal. The input is a list containing elements of any type, including nested lists. The output should be a list with the same structure as the input, but with no duplicate elements or sublists.
"""

def remove_duplicates(nested_list):
    seen = set()
    output_list = []
    
    for item in nested_list:   
        # If item is a list, call the function recursively
        if isinstance(item, list):   
            item = remove_duplicates(item)
            if str(item) not in seen:
                output_list.append(item)
                seen.add(str(item))
        # If item is a unique element, add to the output list
        elif item not in seen:
            output_list.append(item)
            seen.add(item)
    
    return output_list