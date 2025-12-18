"""
QUESTION:
Implement a function named `custom_hash` that computes a custom hash code for a given string. The function should take into account both the characters and the length of the string.
"""

def custom_hash(string):
    hash_value = 0
    hash_value += len(string) * 31
    for char in string:
        hash_value += ord(char) * 17
    return hash_value