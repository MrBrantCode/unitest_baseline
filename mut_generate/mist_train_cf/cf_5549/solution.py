"""
QUESTION:
Write a function `count_common_characters` that takes two strings as input and returns the number of unique common characters between the two strings. The function should be case-sensitive and should not use any built-in string methods or data structures such as lists or dictionaries, except for indexing and concatenation. If either string contains non-alphabetic characters or is empty, the function should return an error message.
"""

def count_common_characters(string_1, string_2):
    if not string_1.isalpha() or not string_2.isalpha():
        return "Error: Strings contain non-alphabetic characters"
    
    common_chars = ""
    for char in string_1:
        if char in string_2 and char not in common_chars:
            common_chars += char
    
    return len(common_chars)