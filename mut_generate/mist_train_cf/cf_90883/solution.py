"""
QUESTION:
Create a function named `sort_data` that takes a list of dictionaries as input, where each dictionary contains 'public_id' and 'name' keys. The function should sort the list in descending order based on 'public_id'. In cases where multiple dictionaries have the same 'public_id', they should be sorted in ascending order based on 'name'. The function should return the sorted list.
"""

def sort_data(data):
    return sorted(data, key=lambda x: (-x['public_id'], x['name']))