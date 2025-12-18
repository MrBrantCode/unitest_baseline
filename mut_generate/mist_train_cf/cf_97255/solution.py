"""
QUESTION:
Write a function named `convert_text` that takes a string `text` as input, converts all vowels in the string to lowercase, removes non-vowel characters, and returns the resulting string with vowels in reverse order.
"""

def convert_text(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            result += char.lower()
    
    return result[::-1]