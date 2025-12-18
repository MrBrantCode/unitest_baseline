"""
QUESTION:
Create a function called `remove_duplicates` that takes a string as input. The function should return a string with all duplicate characters removed, sorted in reverse order, and only consisting of lowercase letters. The resulting string must have a length between 5 and 20 characters.
"""

def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char.islower() and char not in unique_chars:
            unique_chars.append(char)
    unique_chars.sort(reverse=True)
    return ''.join(unique_chars)[:20]