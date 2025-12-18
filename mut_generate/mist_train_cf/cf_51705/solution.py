"""
QUESTION:
Create a function called `validate_hello` that takes a string of characters as input and returns `True` if the string contains the word "hello" (case-insensitive) and `False` otherwise. The function should consider "hello" as a substring, meaning it can appear anywhere in the input string and be part of a larger word.
"""

def validate_hello(chars):
    return 'hello' in chars.lower()