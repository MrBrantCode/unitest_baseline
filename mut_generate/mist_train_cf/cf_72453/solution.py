"""
QUESTION:
Create a function called `convert_to_json` that takes three parameters: `name`, `age`, and `location`, and returns a JSON representation of the input data. The function should be able to handle any valid string for `name` and `location`, and any valid integer for `age`. The output should be a JSON string with the keys "name", "age", and "location" and corresponding values.
"""

import json

def convert_to_json(name, age, location):
    person = {
        "name": name,
        "age": age,
        "location": location
    }
    json_str = json.dumps(person)
    return json_str