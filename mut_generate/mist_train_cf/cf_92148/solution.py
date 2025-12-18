"""
QUESTION:
Create a function `greet` that takes a string parameter `name`. The `name` should be a non-empty string containing only alphabetic characters with a maximum length of 20 characters. If the input is valid, return the string 'Hello name!'. If not, return 'Invalid name!'.
"""

def greet(name):
    if not name or not name.isalpha() or len(name) > 20:
        return "Invalid name!"
    return "Hello " + name + "!"