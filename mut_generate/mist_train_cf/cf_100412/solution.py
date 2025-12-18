"""
QUESTION:
Create a function named `split_string_into_words` that takes a string as input and returns a new string where each word is separated by a space. The function should split the input string into words by inserting a space before each uppercase letter, excluding the first character.
"""

def split_string_into_words(input_string):
    words = ""
    for i, char in enumerate(input_string):
        if i != 0 and char.isupper():
            words += " "
        words += char
    return words