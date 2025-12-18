"""
QUESTION:
Write a function `get_list_length` that calculates the total count of elements in a given list, including elements in nested lists, without using any built-in length functions or methods. The function should take two parameters: the list to calculate the length of, and the current depth level (defaulting to 1). The function should recursively handle nested lists up to a maximum depth of 5 levels.
"""

def get_list_length(lst, depth=1):
    count = 0
    
    for item in lst:
        if isinstance(item, list) and depth < 5:
            count += get_list_length(item, depth + 1)
        else:
            count += 1
    
    return count