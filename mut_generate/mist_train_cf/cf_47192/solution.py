"""
QUESTION:
Develop a function named `merge_strings` that takes two distinct text strings as input and returns a composite string that is the concatenation of the two input strings with a space in between. If the input strings are not distinct, the function should return the message "The strings are not distinct!".
"""

def merge_strings(string1, string2):
    # Checks if the two strings are distinct
    if string1 != string2:
        # Merges the two strings into one with a space in between
        composite_string = string1 + " " + string2
        return composite_string
    else:
        return "The strings are not distinct!"