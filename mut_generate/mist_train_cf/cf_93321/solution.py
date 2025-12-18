"""
QUESTION:
Write a function `convert_to_uppercase_without_vowels` that takes a string as input and returns a new string where all characters are in uppercase and all vowels (both lowercase and uppercase) are excluded.
"""

def convert_to_uppercase_without_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    
    for char in string:
        if char.lower() not in vowels:
            result += char.upper()
    
    return result