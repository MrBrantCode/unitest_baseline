"""
QUESTION:
Convert a dictionary with a date string to a JSON string, converting the date to ISO 8601 format. 

Create a function named `convert_to_json` that takes a dictionary with the keys "firstname", "lastname", and "birthdate" as input, where "birthdate" is in the format "dd-mm-yyyy". The function should return a JSON string with the date in ISO 8601 format ("yyyy-mm-dd").
"""

import json
from datetime import datetime

def convert_to_json(data):
    """
    Convert a dictionary with a date string to a JSON string, converting the date to ISO 8601 format.

    Args:
        data (dict): A dictionary with keys "firstname", "lastname", and "birthdate".

    Returns:
        str: A JSON string with the date in ISO 8601 format.
    """
    # Convert the birthdate to ISO 8601 format
    birthdate = datetime.strptime(data["birthdate"], "%d-%m-%Y")
    data["birthdate"] = birthdate.strftime("%Y-%m-%d")

    # Convert the array to JSON
    return json.dumps(data)