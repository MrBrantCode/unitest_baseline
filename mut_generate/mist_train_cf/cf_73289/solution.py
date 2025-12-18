"""
QUESTION:
Write a function `remove_string` that takes a nested list and a target string as input. The function should recursively remove all occurrences of the target string from the nested list and return the modified list. If the target string is not found in the list, the function should return the original list. The input list can contain both single strings and other nested lists.
"""

def remove_string(nested_list, target):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            new_list = remove_string(item, target)
            if new_list:
                result.append(new_list)
        elif item != target:
            result.append(item)
    return result