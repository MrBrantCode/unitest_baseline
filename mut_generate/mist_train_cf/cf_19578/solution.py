"""
QUESTION:
Implement a function named `remove_duplicates` that takes a string as input, removes consecutive duplicate characters, and returns the modified string.
"""

def remove_duplicates(string):
    result = ""
    last_seen = None
    
    for char in string:
        if char != last_seen:
            result += char
            last_seen = char
    
    return result