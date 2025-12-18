"""
QUESTION:
Create a function named `reverse_tuple_string` that takes a tuple of words as input and returns a string with the words in reverse order, all letters in uppercase, and without punctuation marks. The function should be implemented in one line of code.
"""

def reverse_tuple_string(tuple_to_string):
    return " ".join(tuple_to_string[::-1]).upper().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "")