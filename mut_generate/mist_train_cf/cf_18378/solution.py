"""
QUESTION:
Write a function named `convert_string` that takes a string as input and returns the modified string where each non-vowel character is converted to upper case and each vowel character is converted to lower case. The function should handle both lower and upper case vowels.
"""

def convert_string(string):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char.lower() in vowels:
            result += char.lower()
        else:
            result += char.upper()
    return result