"""
ORIGINAL QUESTION:
Create a Python function `organize_list` that takes a list of dictionaries as input and returns a new list where the dictionaries are sorted in ascending order by a specified key. The function should be able to sort by any key present in the dictionaries, such as 'age' or 'name'.
"""

def organize_list(list_dict, key):
    return sorted(list_dict, key=lambda x: x[key])