"""
QUESTION:
Implement the `encode_json` and `decode_json` functions. The `encode_json` function should take in a JSON object and an optional property name, and return the Base64 encoded JSON object if no property name is specified, or modify the JSON object in-place to encode the specified property if a property name is specified. The `decode_json` function should take in a Base64 encoded JSON object and an optional property name, and return the decoded JSON object if no property name is specified, or modify the JSON object in-place to decode the specified property if a property name is specified. The functions should also handle the case where the specified property does not exist in the JSON object.
"""

import json
import base64

# Function to encode a JSON object using Base64
def encode_json(json_obj, property_name=None):
    if property_name:
        if property_name in json_obj:
            json_obj[property_name] = base64.b64encode(str(json_obj[property_name]).encode()).decode()
        else:
            print("Property not found in JSON object.")
    else:
        json_str = json.dumps(json_obj)
        json_obj_encoded = base64.b64encode(json_str.encode()).decode()
        return json_obj_encoded

# Function to decode a Base64 encoded JSON object
def decode_json(json_obj_encoded, property_name=None):
    if property_name:
        if property_name in json_obj_encoded:
            json_obj_encoded[property_name] = base64.b64decode(str(json_obj_encoded[property_name]).encode()).decode()
        else:
            print("Property not found in Base64 encoded JSON object.")
    else:
        json_str = base64.b64decode(json_obj_encoded.encode()).decode()
        json_obj = json.loads(json_str)
        return json_obj