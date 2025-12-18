"""
QUESTION:
Write a function `remove_extra_spaces(s)` that takes a string `s` as input, removes any leading or trailing spaces, and ensures there is exactly one space between words.
"""

def remove_extra_spaces(s):
    s = s.strip()
    words = s.split(" ")
    result = ""
    for word in words:
        if word:
            result += word + " "
    return result.strip()