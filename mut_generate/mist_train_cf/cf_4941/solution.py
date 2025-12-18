"""
QUESTION:
Write a function called `convert_string` that takes a string as input. The function should convert all uppercase letters to lowercase, remove all vowels from the string, and then reverse the order of the remaining letters. The input string is assumed to only contain alphabets.
"""

def convert_string(text):
    # Convert the string to lowercase
    text = text.lower()

    # Remove vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = ''.join([char for char in text if char not in vowels])

    # Reverse the order of the remaining letters
    text = text[::-1]

    return text