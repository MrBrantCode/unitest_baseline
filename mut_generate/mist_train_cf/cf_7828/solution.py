"""
QUESTION:
Write a function `check_key_exists(dictionary, key)` that checks if a given key exists in a nested dictionary or not. The function should be case-insensitive, handle keys with leading or trailing spaces, and keys with spaces before or after the dots. The function should use recursion and not utilize any built-in Python functions or libraries. The function should return "Key exists" if the key exists, and "Key does not exist" otherwise. The input `dictionary` is a nested dictionary and `key` is a string that represents the key to be checked.
"""

def check_key_exists(dictionary, key):
    if "." in key:
        key, rest = key.split(".", 1)
        key = key.strip()
        if key.lower() in dictionary:
            return check_key_exists(dictionary[key.lower()], rest)
    key = key.strip()
    if key.lower() in dictionary:
        return "Key exists"
    return "Key does not exist"