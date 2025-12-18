"""
QUESTION:
Write a function named `remove_duplicates` that takes a string as input, removes duplicate characters while preserving the original order of characters, and returns the result. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the string.
"""

def remove_duplicates(string):
    unique_chars = set()
    result = ""
    
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    
    return result