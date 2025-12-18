"""
QUESTION:
Create a function 'greet' that takes a string parameter 'name'. The function should return 'Hello name!' if 'name' is a non-empty string containing only alphabetic characters, has a maximum length of 10 characters, and is in all uppercase letters. Otherwise, the function should return an empty string.
"""

def greet(name):
    if len(name) > 10 or not name.isalpha() or not name.isupper():
        return ""
    else:
        return "Hello {}!".format(name)