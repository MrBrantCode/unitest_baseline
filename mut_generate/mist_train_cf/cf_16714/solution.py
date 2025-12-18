"""
QUESTION:
Write a function `access_nested_name` that takes a dictionary as input. The dictionary contains a key 'age' and a key 'nested_list' that stores a list of dictionaries. The function should return the value of the key 'name' from the last dictionary in the 'nested_list' if the list has more than two elements and the value of the key 'age' in the input dictionary is less than 30. If the conditions are not met, the function should return "Conditions not satisfied or value not found".
"""

def access_nested_name(data):
    """
    Access the value of the key 'name' from the last dictionary in the 'nested_list'
    if the list has more than two elements and the value of the key 'age' in the input dictionary is less than 30.

    Args:
        data (dict): The input dictionary containing 'age' and 'nested_list'.

    Returns:
        str: The value of the key 'name' or "Conditions not satisfied or value not found".
    """
    if len(data.get('nested_list', [])) > 2 and data.get('age', 0) < 30:
        nested_list = data.get('nested_list', [])
        last_dict = nested_list[-1] if nested_list else {}
        return last_dict.get('name', "Conditions not satisfied or value not found")
    return "Conditions not satisfied or value not found"