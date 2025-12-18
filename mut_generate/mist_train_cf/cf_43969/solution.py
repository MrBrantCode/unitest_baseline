"""
QUESTION:
Create a function named `generate_json_structure` that generates a JSON structure for a user containing their full name, age, address, a list of favorite programming languages in order of preference, and a set of key-value pairs for hobbies and hours spent per week. The function should return the JSON string with proper indentation.
"""

import json

def generate_json_structure(name, full_name, age, address, favorite_languages, hobbies):
    data = {
        name: {
            "Full Name": full_name,
            "Age": age,
            "Address": address,
            "Favorite Programming Languages": favorite_languages,
            "Hobbies": hobbies
        }
    }
    return json.dumps(data, indent=4)