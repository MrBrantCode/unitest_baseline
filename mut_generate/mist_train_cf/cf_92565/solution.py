"""
QUESTION:
Construct a function `encrypt_and_construct_json` that constructs a JSON object with encrypted "name" and "age" parameters. The function should take two parameters: `name` and `age`. The "name" and "age" parameters should be encrypted using a custom encryption algorithm before being included in the JSON object. The encrypted values should be valid strings that can be decrypted back to their original values. The function should return the JSON object as a string.
"""

import json

def encrypt_and_construct_json(name, age):
    # Custom encryption algorithm (you can replace this with your own)
    encrypted_name = name[::-1]  # reverse the string
    encrypted_age = str(age)[::-1]  # reverse the string

    # Construct the JSON object
    json_object = {
        "encrypted_name": encrypted_name,
        "encrypted_age": encrypted_age
    }

    # Serialize the JSON object
    return json.dumps(json_object)