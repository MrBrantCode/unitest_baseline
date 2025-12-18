"""
QUESTION:
Write a function `transform_string` that takes a string `input_string` of length between 1 and 1000, containing only alphabetic characters, as input. The function should return a string where all vowels (a, e, i, o, u) are converted to uppercase and all consonants are converted to lowercase.
"""

def transform_string(input_string):
    vowels = "aeiou"
    result = ""
    for char in input_string:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result += char.lower()
    return result