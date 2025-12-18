"""
QUESTION:
Your dad doesn't really *get* punctuation, and he's always putting extra commas in when he posts. You can tolerate the run-on sentences, as he does actually talk like that, but those extra commas have to go!

Write a function called ```dadFilter``` that takes a string as argument and returns a string with the extraneous commas removed. The returned string should not end with a comma or any trailing whitespace.
"""

from re import compile, sub

# Compile the regex pattern for one or more commas
REGEX = compile(',+')

def dad_filter(strng: str) -> str:
    """
    Filters out extraneous commas from the input string and removes any trailing commas or whitespace.

    Parameters:
    - strng (str): The input string that may contain extraneous commas.

    Returns:
    - str: The filtered string with extraneous commas removed and no trailing commas or whitespace.
    """
    # Replace one or more commas with a single comma
    filtered_str = sub(REGEX, ',', strng)
    # Remove any trailing commas or whitespace
    return filtered_str.rstrip(' ,')