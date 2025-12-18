"""
QUESTION:
Create a function called `concatenate_strings` that takes two strings as input, `str1` and `str2`. The function should return a concatenated string containing characters from `str1` that are also present in `str2`, with each character appearing only once in the order they appear in `str1`, all in lowercase, and with all vowels removed.
"""

def concatenate_strings(str1, str2):
    concat = ""
    for char in str1:
        if char.lower() in str2.lower() and char.lower() not in concat:
            concat += char.lower()
    return "".join([c for c in concat if c.lower() not in "aeiou"])