"""
QUESTION:
Create a function `surrounded_substring_regex` that takes three parameters: `string`, `substring`, `starting_characters`, and `ending_characters`. The function should return a regular expression pattern that matches all occurrences of `substring` in `string` if and only if each occurrence of `substring` is surrounded by `starting_characters` and `ending_characters`.
"""

import re

def surrounded_substring_regex(string, substring, starting_characters, ending_characters):
    """
    Returns a regular expression pattern that matches all occurrences of substring in string 
    if and only if each occurrence of substring is surrounded by starting_characters and ending_characters.

    Parameters:
    string (str): The string to search in.
    substring (str): The substring to search for.
    starting_characters (str): The characters that must precede the substring.
    ending_characters (str): The characters that must follow the substring.

    Returns:
    list: A list of all occurrences of substring in string that are surrounded by starting_characters and ending_characters.
    """
    pattern = f"(?<={re.escape(starting_characters)}){re.escape(substring)}(?={re.escape(ending_characters)})"
    return re.findall(pattern, string)