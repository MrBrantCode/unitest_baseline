"""
QUESTION:
Write a function named `find_input_for_hash` that takes an integer `hash_size` as input and returns a tuple containing the SHA-256 hash and the original input string that produced it, where the length of the hash string is equal to the given `hash_size`.
"""

import hashlib

def find_input_for_hash(hash_size):
    input_value = 0
    while True:
        input_str = str(input_value)
        hash_value = hashlib.sha256(input_str.encode()).hexdigest()
        if len(hash_value) == hash_size:
            return hash_value, input_str
        input_value += 1