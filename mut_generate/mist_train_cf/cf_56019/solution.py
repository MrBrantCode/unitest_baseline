"""
QUESTION:
Write a function `mirror_text_feed(input_string)` that takes a string as input, removes any non-alphabetic characters, and returns the resulting string in reverse order.
"""

def mirror_text_feed(input_string):
    input_string = ''.join(e for e in input_string if e.isalpha())
    return input_string[::-1]