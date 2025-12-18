"""
QUESTION:
Write a function called `remove_repetitive_digits` that takes a string of consecutive numerical characters as input and returns a new string with all successive, recurring digits removed.
"""

def remove_repetitive_digits(input_string):
    prev_char = ""
    new_string = ""
    for char in input_string:
        if char != prev_char:
            new_string += char
        prev_char = char
    return new_string