"""
QUESTION:
Write a function `to_camel_case(text)` that takes a string as input, where the string is in underscore notation, and returns the string converted to camelCase format. The function should remove underscores and capitalize the first letter of each word except the first word.
"""

def to_camel_case(text):
    text = text.split('_')
    for i in range(1, len(text)):
        text[i] = text[i].title()
    return ''.join(text)