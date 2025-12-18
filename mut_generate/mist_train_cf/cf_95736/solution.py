"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input, removes all consecutive duplicate characters, and returns the modified string. If the input string is empty or contains no consecutive duplicate characters, return the original string.
"""

def remove_duplicates(string):
    result = ""
    last_seen = None
    
    for char in string:
        if char != last_seen:
            result += char
            last_seen = char
    
    return result