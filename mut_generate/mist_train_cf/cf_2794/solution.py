"""
QUESTION:
Write a function named `get_keys` that takes a dictionary as input and returns a list of keys. Each key in the returned list should appear twice, and the function should exclude keys that start with a vowel (case-insensitive) and keys that contain special characters or numbers. The function should only include keys that consist entirely of alphabetic characters and start with a consonant.
"""

def get_keys(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    keys = []
    
    for key in dictionary.keys():
        if key[0].lower() not in vowels and key.isalpha():
            keys.extend([key, key])
    
    return keys