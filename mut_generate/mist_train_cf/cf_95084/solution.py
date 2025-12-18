"""
QUESTION:
Write a function `sort_dict_list` that sorts a list of dictionaries in descending order based on the 'age' key. If two or more dictionaries have the same age, they should be further sorted in ascending order based on the 'name' key. The function should return the sorted list of dictionaries.
"""

def sort_dict_list(dict_list):
    return sorted(dict_list, key=lambda x: (-x['age'], x['name']))