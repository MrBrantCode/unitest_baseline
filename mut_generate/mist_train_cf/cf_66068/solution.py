"""
QUESTION:
Create a function `dict_to_json(dictionary)` that takes a dictionary as input and returns a JSON-formatted string. The dictionary is expected to contain the keys 'name', 'age', 'address', and 'dependants'. The 'dependants' key should have a list of dictionaries with the keys 'name' and 'age'. The function should implement exception handling to handle cases where any of the expected keys are missing. If a key is missing, it should print an error message indicating the missing key and continue executing without terminating.
"""

import json

def dict_to_json(dictionary):
    try:
        name = dictionary['name']
        age = dictionary['age']
        address = dictionary['address']
        dependants = dictionary['dependants']
        for dependant in dependants:
            dependant_name = dependant['name']
            dependant_age = dependant['age']
        return json.dumps(dictionary)
    except KeyError as e:
        print(f"Missing key: {e}")