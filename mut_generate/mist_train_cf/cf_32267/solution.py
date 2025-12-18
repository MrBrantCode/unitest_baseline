"""
QUESTION:
Write a function `count_unique_characters` that takes a string as input and returns a dictionary containing the count of each unique alphabetic character in the string, ignoring whitespace and case differences.
"""

def entance(s: str) -> dict:
    char_count = {}
    s = s.lower().replace(" ", "")  
    for char in s:
        if char.isalpha():  
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count