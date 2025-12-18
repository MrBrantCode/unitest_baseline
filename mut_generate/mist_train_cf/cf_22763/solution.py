"""
QUESTION:
Create a function `convert_text` that takes a string as input and returns a string where all vowels are converted to lowercase and their order is reversed, while non-vowel characters are excluded from the output.
"""

def convert_text(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            result += char.lower()
    
    return result[::-1]