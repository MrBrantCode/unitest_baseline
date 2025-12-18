"""
QUESTION:
Write a function `generate_hash` that generates a SHA-256 hash for a given string. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1). Additionally, implement a function `check_hash` that checks if the generated hash matches a given hash. The `check_hash` function should have a time complexity of O(1). The functions should handle both lowercase and uppercase characters, non-alphanumeric characters, and Unicode characters in the input string.
"""

import hashlib

def generate_hash(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

def check_hash(string, given_hash):
    generated_hash = generate_hash(string)
    return generated_hash == given_hash