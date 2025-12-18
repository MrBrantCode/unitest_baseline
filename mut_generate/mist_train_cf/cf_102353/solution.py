"""
QUESTION:
Write a function `find_strings(list_of_strings, target_string)` that takes a list of strings and a target string as input, and returns a list of strings which contain the target string as a substring. The target string must be at least 5 characters long and contain only lowercase letters. The function should return an empty list if the target string does not meet these requirements. The order of the strings in the output list should be the same as the order of their occurrences in the input list.
"""

def entrance(list_of_strings, target_string):
    if len(target_string) < 5 or not target_string.islower():
        return []
    
    result = []
    for string in list_of_strings:
        if target_string in string:
            result.append(string)
    
    return result