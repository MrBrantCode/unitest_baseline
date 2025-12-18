"""
QUESTION:
Construct a function `sort_data` that sorts a list of dictionaries by 'name' in ascending order, and for entries with the same 'name', sorts them by 'public_id' in descending order.
"""

def sort_data(data):
    return sorted(data, key=lambda x: (x['name'], -x['public_id']))