"""
QUESTION:
Create a function `construct_json_object` that constructs a JSON object with the following structure and sample values: 
- "name" as string
- "age" as integer
- "email" as string
- "address" as an object containing "street", "city", "state", and "zipcode"
- "hobbies" as an array of strings
- "education" as an object containing "school", "major", and "year"
- "friends" as an array of objects containing "name", "age", and "email".
"""

import json

def construct_json_object(name, age, email, street, city, state, zipcode, 
                          hobbies, school, major, year, friends):
    """
    Construct a JSON object with the given parameters.

    Args:
    - name (str): The person's name.
    - age (int): The person's age.
    - email (str): The person's email.
    - street (str): The person's street address.
    - city (str): The person's city.
    - state (str): The person's state.
    - zipcode (str): The person's zipcode.
    - hobbies (list): A list of the person's hobbies.
    - school (str): The person's school.
    - major (str): The person's major.
    - year (int): The person's year of graduation.
    - friends (list): A list of dictionaries containing friends' information.

    Returns:
    - A JSON string representing the constructed JSON object.
    """

    data = {
        "name": name,
        "age": age,
        "email": email,
        "address": {
            "street": street,
            "city": city,
            "state": state,
            "zipcode": zipcode
        },
        "hobbies": hobbies,
        "education": {
            "school": school,
            "major": major,
            "year": year
        },
        "friends": friends
    }

    return json.dumps(data, indent=2)