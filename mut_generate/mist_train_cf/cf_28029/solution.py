"""
QUESTION:
Implement the `encode_json_data` function, which takes a JSON-formatted dictionary as input and returns the encoded output. The encoding scheme is as follows: encode all keys and string values using Base64 encoding, and multiply all integer values by 2. The function should handle dictionaries with various types of values and return the encoded output. The function signature is `def encode_json_data(json_data: dict) -> any`.
"""

import base64

def encode_json_data(json_data: dict) -> dict:
    encoded_data = {}
    for key, value in json_data.items():
        encoded_key = base64.b64encode(key.encode('utf-8')).decode('utf-8')
        if isinstance(value, str):
            encoded_data[encoded_key] = base64.b64encode(value.encode('utf-8')).decode('utf-8')
        elif isinstance(value, int):
            encoded_data[encoded_key] = value * 2
        elif isinstance(value, dict):
            encoded_data[encoded_key] = encode_json_data(value)
        else:
            encoded_data[encoded_key] = value  
    return encoded_data