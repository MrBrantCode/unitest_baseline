"""
QUESTION:
Create a function named `capitalize_words` that takes a string of lowercase words separated by spaces as input and returns a new string with the first character of each word capitalized.
"""

def capitalize_words(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)