"""
QUESTION:
Write a Python function `generate_token(payload: dict) -> str` that takes a dictionary as input, extracts the values of keys "username", "timestamp", and "random", concatenates these values in the format "username:timestamp:random", applies the SHA-256 hashing algorithm to the concatenated string, and returns the token as a hexadecimal string. The input dictionary is guaranteed to contain the required keys, but the function should be able to handle missing keys by using empty strings as default values.
"""

import hashlib

def generate_token(payload: dict) -> str:
    username = payload.get("username", "")
    timestamp = payload.get("timestamp", "")
    random = payload.get("random", "")

    concatenated_string = f"{username}:{timestamp}:{random}"
    hashed_token = hashlib.sha256(concatenated_string.encode()).hexdigest()

    return hashed_token