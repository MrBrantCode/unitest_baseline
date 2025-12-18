"""
QUESTION:
Write a Python function named `get_keys` that takes a dictionary as input and returns a list of keys from the dictionary. Each key in the output list should appear twice. The function should ignore any keys that start with a vowel ('a', 'e', 'i', 'o', 'u') and any keys that contain special characters or numbers.
"""

def get_keys(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    keys = []
    
    for key in dictionary.keys():
        if key[0].lower() not in vowels and key.isalpha():
            keys.extend([key, key])
    
    return keys