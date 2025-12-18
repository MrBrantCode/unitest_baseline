"""
QUESTION:
Create a function `sort_data` that takes a list of dictionaries as input, where each dictionary has 'name' and 'popularity' keys. Sort the list in the following order: 
1. Dictionaries with a 'popularity' value of 3 or more in descending order, 
2. Then by 'name' in ascending order for dictionaries with the same 'popularity' value, 
3. Finally, dictionaries with a 'popularity' value less than 3 at the end.
"""

def sort_data(data):
    """
    Sorts a list of dictionaries based on 'popularity' and 'name' keys.
    
    The list is sorted in the following order:
    1. Dictionaries with a 'popularity' value of 3 or more in descending order,
    2. Then by 'name' in ascending order for dictionaries with the same 'popularity' value,
    3. Finally, dictionaries with a 'popularity' value less than 3 at the end.
    
    Args:
        data (list): A list of dictionaries containing 'name' and 'popularity' keys.
    
    Returns:
        list: The sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: (x['popularity'] < 3, -x['popularity'], x['name']))