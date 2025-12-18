"""
QUESTION:
Write a function `updated_hash_func` that takes a string `s` as input and returns its hash code. The function should adhere to the principles of a good hash function: it should be able to handle a multitude of strings regardless of their length or characters, and it should be case-insensitive. The function should also handle collisions efficiently.
"""

def updated_hash_func(s):
    hash = 5381
    s = s.lower()               # Make it case-insensitive
    for char in s:
        hash = ((hash << 5) + hash) + ord(char)
    return hash & 0xFFFFFFFFFFFFFFFF   # Return a 64-bit hash value