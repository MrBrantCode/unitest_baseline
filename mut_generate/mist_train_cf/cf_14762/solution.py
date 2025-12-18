"""
QUESTION:
Write a function named `update_text` that takes a string as input. If the length of the input string is greater than 5 characters, the function should return the string "Hello World". Otherwise, it should return the original string.
"""

def update_text(text):
    if len(text) > 5:
        return "Hello World"
    else:
        return text