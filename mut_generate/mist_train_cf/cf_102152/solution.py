"""
QUESTION:
Create a function `create_json_object` to generate a properly formatted JSON object with the following fields: name (string), age (integer), occupation (string), address (nested object with street, city, country), hobbies (list of strings), and education (string).
"""

import json

def create_json_object(name, age, occupation, street, city, country, hobbies, education):
    """
    Creates a properly formatted JSON object with the given fields.

    Args:
    name (str): The person's name.
    age (int): The person's age.
    occupation (str): The person's occupation.
    street (str): The street of the person's address.
    city (str): The city of the person's address.
    country (str): The country of the person's address.
    hobbies (list): A list of the person's hobbies.
    education (str): The person's education.

    Returns:
    str: A JSON object with the given fields.
    """

    details = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "address": {
            "street": street,
            "city": city,
            "country": country
        },
        "hobbies": hobbies,
        "education": education
    }

    return json.dumps(details, indent=4)