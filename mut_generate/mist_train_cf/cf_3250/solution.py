"""
QUESTION:
Create a function `capitalize_words(string)` that takes a string of multiple words separated by spaces as input and returns a new string with the first character of each word capitalized. The input string may contain punctuation marks.
"""

def capitalize_words(string):
    # Split the string into a list of words
    words = string.split()

    # Capitalize the first character of each word and join them back into a string
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = ' '.join(capitalized_words)

    return capitalized_string