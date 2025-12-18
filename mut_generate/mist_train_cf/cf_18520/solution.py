"""
QUESTION:
Write a function `count_unique_chars` that takes a string as input and returns the number of unique characters in the string. The function should not use any additional data structures (such as sets, lists, dictionaries, etc.) or built-in string or array manipulation functions.
"""

def count_unique_chars(string):
    count = 0
    unique_chars = ""
    
    for char in string:
        if char not in unique_chars:
            count += 1
            unique_chars += char
    
    return count