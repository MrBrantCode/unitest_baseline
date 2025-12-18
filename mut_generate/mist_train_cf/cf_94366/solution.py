"""
QUESTION:
Create a function named `access_nested_name` that takes a dictionary as input and returns the value of the key 'name' if it exists in the nested list of dictionaries. The function should only return the 'name' value if the length of the list is greater than 2 and the value of the key 'age' in the outer dictionary is less than 30.
"""

def access_nested_name(data):
    """
    Access the value of the key 'name' in the nested list of dictionaries.

    Args:
        data (dict): The dictionary containing the nested list.

    Returns:
        str: The value of the key 'name' if conditions are satisfied, otherwise None.
    """
    # Check if the length of the list is greater than 2 and the value of the key 'age' in the outer dictionary is less than 30.
    if len(data.get('nested_list', [])) > 2 and data.get('age', 0) < 30:
        # Access the list stored in the outer dictionary using its key.
        nested_list = data['nested_list']
        # Access the nested dictionary within the list using its index.
        nested_dict = nested_list[2]
        # Access the value of the key 'name' in the nested dictionary.
        return nested_dict.get('name')
    else:
        return None