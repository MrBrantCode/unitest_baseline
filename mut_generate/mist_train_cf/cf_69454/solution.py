"""
QUESTION:
Create a function `sort_data` that sorts a list of dictionaries in descending order by the 'public_id' key and in ascending order by the 'name' key when 'public_id' values are the same. The function should take a list of dictionaries as input, where each dictionary contains 'name' and 'public_id' keys.
"""

def sort_data(data):
    return sorted(data, key=lambda x: (-x['public_id'], x['name']))