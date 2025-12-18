"""
QUESTION:
Create a function `capitalize_words(input_string)` that takes a string of multiple words separated by spaces as input, where the input string is in lowercase and does not contain any punctuation marks. The function should return a new string with the first character of each word capitalized.
"""

def capitalize_words(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)