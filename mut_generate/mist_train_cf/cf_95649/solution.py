"""
QUESTION:
Create a function 'greet' that takes a string parameter 'name' and returns 'Hello name!' if the following conditions are met: 'name' contains only alphabetic characters, has a maximum length of 10 characters, and is in all uppercase letters. Otherwise, return an empty string.
"""

def greet(name):
    if len(name) > 10 or not name.isalpha() or not name.isupper():
        return ""
    else:
        return "Hello {}!".format(name)