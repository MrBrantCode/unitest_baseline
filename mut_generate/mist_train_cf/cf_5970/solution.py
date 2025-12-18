"""
QUESTION:
Write a function `get_age_data_type` that takes a JSON object as input and returns the data type of the value associated with the "age" key, handling cases where the key may not exist or have a different data type. The function should return `None` if the key does not exist.
"""

def get_age_data_type(json_obj):
    """
    Returns the data type of the value associated with the "age" key in a JSON object.

    Args:
        json_obj (dict): The input JSON object.

    Returns:
        type or None: The data type of the "age" value if it exists, otherwise None.
    """
    return type(json_obj.get("age"))