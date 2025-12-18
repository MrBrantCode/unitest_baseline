"""
QUESTION:
Write a function named `remove_duplicates` that takes a string as input, removes duplicate characters while keeping only lowercase letters, sorts the resulting string in reverse order, and returns a substring of the sorted string with a maximum length of 20 characters, ensuring the returned string has a length of at least 5 characters.
"""

def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char.islower() and char not in unique_chars:
            unique_chars.append(char)
    unique_chars.sort(reverse=True)
    return ''.join(unique_chars)[:20]