"""
QUESTION:
Write a function named 'sort_names' that takes a list of dictionaries as input where each dictionary contains a 'name' key. Return a sorted list of unique names. The function should handle cases where a name may appear more than once or not exist at all. The input list of dictionaries should not contain duplicate keys.
"""

def sort_names(name_list):
    sorted_unique_names = []
    for n in name_list:
        if n['name'] not in sorted_unique_names:
            sorted_unique_names.append(n['name'])
    sorted_unique_names.sort()
    return sorted_unique_names