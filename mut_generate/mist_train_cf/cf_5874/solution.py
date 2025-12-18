"""
QUESTION:
Write a function `remove_carrots` that takes a list of strings as input and returns the modified list with all elements with the value "Carrots" removed, except for the first occurrence. The input list may be empty and can contain up to 1000 elements, all of which will be strings of lowercase alphabetical characters.
"""

def remove_carrots(lst):
    if not lst:
        return []
    
    result = []
    has_carrots = False
    for element in lst:
        if element == "Carrots":
            if not has_carrots:
                result.append(element)
                has_carrots = True
        else:
            result.append(element)
    
    return result