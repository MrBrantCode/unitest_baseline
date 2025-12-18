"""
QUESTION:
Create two functions, `get_location` and `get_age_and_gender`, to extract information from a JSON data object. 

Function `get_location` should take a JSON data object as input and return a dictionary with "city", "state", and "country" values converted to lowercase.

Function `get_age_and_gender` should take a JSON data object as input and return a string containing the "age" and "gender" values concatenated together. The "age" value should be converted to a string.
"""

def get_location(data):
    """
    Extracts location information from a JSON data object and returns a dictionary 
    with "city", "state", and "country" values converted to lowercase.

    Args:
        data (dict): A JSON data object.

    Returns:
        dict: A dictionary containing "city", "state", and "country" values in lowercase.
    """
    return {
        "city": data["location"]["city"].lower(),
        "state": data["location"]["state"].lower(),
        "country": data["location"]["country"].lower()
    }

def get_age_and_gender(data):
    """
    Retrieves the values of "age" and "gender" from a JSON data object and returns 
    them as a concatenated string.

    Args:
        data (dict): A JSON data object.

    Returns:
        str: A string containing the "age" and "gender" values.
    """
    return str(data["age"]) + " " + data["gender"]