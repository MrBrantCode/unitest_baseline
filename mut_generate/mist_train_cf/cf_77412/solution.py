"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as input. The function should return two outputs: a list of strings with duplicates removed while preserving the original sequence, and a dictionary with the removed strings as keys and their frequency as values.
"""

def remove_duplicates(input_list):
    result = []
    removed_str = {}
    
    for item in input_list:
        if item not in result:
            result.append(item)
        else:
            if item not in removed_str:
                removed_str[item] = 1
            else:
                removed_str[item] += 1
    
    return result, removed_str