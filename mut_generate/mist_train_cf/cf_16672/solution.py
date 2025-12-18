"""
QUESTION:
Create a function `filter_to_dict` that takes an array of objects as input, where each object contains an `id` and a `name`. The function should return a dictionary where the key is the `id` and the value is the `name`, but only include objects that have an even `id` and whose `names` contain the letter 'a'.
"""

def filter_to_dict(arr):
    """
    This function filters an array of objects based on the 'id' and 'name' properties.
    It returns a dictionary where the key is the 'id' and the value is the 'name',
    but only includes objects that have an even 'id' and whose 'names' contain the letter 'a'.

    Parameters:
    arr (list): A list of dictionaries, each containing 'id' and 'name' keys.

    Returns:
    dict: A dictionary where the key is the 'id' and the value is the 'name'.
    """
    return {obj['id']: obj['name'] for obj in arr if obj['id'] % 2 == 0 and 'a' in obj['name']}