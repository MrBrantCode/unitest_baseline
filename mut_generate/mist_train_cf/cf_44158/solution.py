"""
QUESTION:
Create a class named `User` with methods to update and retrieve a dictionary, serialize it to JSON format, and deserialize it back to the dictionary. The dictionary should have initial keys "occupation", "birthday", and "hobby" and should be able to handle additional keys in the future without direct modification to the class. The class should handle the conversion of date objects during JSON serialization and deserialization. The `birthday` should be stored in the format "%d-%m-%Y". 

The class should have the following methods: 
- `__init__(self, occupation, birthday, hobby)`: Initialize the dictionary with the given keys.
- `update_key(self, key, value)`: Update the dictionary with a given key and value.
- `retrieve_dict(self)`: Return the dictionary.
- `to_json(self)`: Serialize the dictionary to JSON format.
- A class method to deserialize a JSON string back to the dictionary.
"""

import json
from datetime import datetime

def entrance(occupation, birthday, hobby, key=None, value=None, json_str=None):
    if json_str:
        data = json.loads(json_str)
        if "birthday" in data:
            data["birthday"] = datetime.strptime(data["birthday"], "%d-%m-%Y")
        user_dict = data
    else:
        user_dict = {
            "occupation": occupation,
            "birthday": birthday.strftime("%d-%m-%Y"),
            "hobby": hobby
        }

    if key:
        if key == "birthday":
            value = value.strftime("%d-%m-%Y")
        user_dict[key] = value

    if json_str:
        return user_dict
    else:
        return json.dumps(user_dict)