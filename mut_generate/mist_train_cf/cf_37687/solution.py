"""
QUESTION:
Write a function `parseOpenCMProperties` that takes a JSON string as input, representing OpenCM Properties, and returns a dictionary containing the extracted information. The dictionary should have the keys "host", "port", "user", and "extended_properties". The "extended_properties" key should map to a list of dictionaries, each representing a property with its name and value. The input JSON string is expected to have the same structure as the provided example.
"""

import json

def parseOpenCMProperties(jsonString):
    data = json.loads(jsonString)
    parsed_data = {
        "host": data["Transport"]["Host"],
        "port": data["Transport"]["Port"],
        "user": data["Auth"]["User"],
        "extended_properties": [{"name": prop["@name"], "value": prop["$"]} for prop in data["ExtendedProperties"]["Property"]]
    }
    return parsed_data