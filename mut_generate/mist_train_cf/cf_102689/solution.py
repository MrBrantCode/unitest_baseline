"""
QUESTION:
Create a method named `sort_data` that takes a list of dictionaries as input, where each dictionary contains 'public_id' and 'name' keys. The method should return the list sorted in descending order by 'public_id', and for dictionaries with the same 'public_id', they should be sorted in ascending order by 'name'.
"""

def sort_data(data):
    sorted_data = sorted(data, key=lambda x: (-x['public_id'], x['name']))
    return sorted_data