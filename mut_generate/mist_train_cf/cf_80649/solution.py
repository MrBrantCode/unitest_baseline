"""
QUESTION:
Create a function called `encode_decode_json` that takes a JSON object as input, encodes it using Base64, decodes the encoded string back into a JSON object, adds a new key-value pair to it, and returns the updated JSON object. The new key-value pair should be "newKey": "newValue".
"""

import json
import base64

def encode_decode_json(json_obj):
    """
    This function takes a JSON object, encodes it using Base64, decodes the encoded string back into a JSON object,
    adds a new key-value pair to it, and returns the updated JSON object.
    
    Args:
    json_obj (dict): The input JSON object.
    
    Returns:
    dict: The updated JSON object with the new key-value pair.
    """
    
    # Convert the JSON object into a string, encode it into bytes, and base64 encode that
    encoded_json = base64.b64encode(json.dumps(json_obj).encode('utf-8'))
    
    # Decode the base64 string, decode the bytes into a string, and load the string into a JSON object
    decoded_json = json.loads(base64.b64decode(encoded_json).decode('utf-8'))
    
    # Add a new key-value pair
    decoded_json["newKey"] = "newValue"
    
    return decoded_json