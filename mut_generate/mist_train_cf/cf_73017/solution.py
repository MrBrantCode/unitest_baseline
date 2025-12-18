"""
QUESTION:
Create a function named `mirror_string` that takes a string `s` as input and returns a new string that starts with "Hola ", followed by the reverse of `s`, and ends with " Hello".
"""

def mirror_string(s):
    return "Hola " + s[::-1] + " Hello"