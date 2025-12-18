"""
QUESTION:
Write a function `to_uppercase(s)` that takes a string `s` as input, checks if the string contains only alphabets and spaces, and returns the string in all uppercase if the condition is met. If the string contains any other characters, return "Invalid input. Please enter a string that contains only alphabets and spaces."
"""

def to_uppercase(s):
    for character in s:
        if not character.isalpha() and not character.isspace():
            return "Invalid input. Please enter a string that contains only alphabets and spaces."

    return s.upper()