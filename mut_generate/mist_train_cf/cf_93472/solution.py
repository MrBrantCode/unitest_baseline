"""
QUESTION:
Write a function `replace_hello` that takes a string as input and returns a new string where "Hello, " is replaced with "Goodbye, ", but only if "Hello, " appears at the beginning of the sentence and is capitalized. The replacement should be case-sensitive.
"""

def replace_hello(string):
    return string.replace("Hello, ", "Goodbye, ")