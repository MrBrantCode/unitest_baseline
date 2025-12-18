"""
QUESTION:
Write a function `convert_string(text)` that takes a string as input, converts all uppercase letters to lowercase, and removes all vowels from the string. The function should return the modified string.
"""

def convert_string(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    converted_text = ""
    
    for char in text:
        if char.isupper():
            char = char.lower()
        
        if char.lower() not in vowels:
            converted_text += char
    
    return converted_text