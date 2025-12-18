"""
QUESTION:
Write a function named `split_string` that takes two parameters, a string and a delimiter, and returns a list of strings where the input string is split by the given delimiter. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string(string, delimiter):
    result = []
    current_word = ""
    
    for char in string:
        if char == delimiter:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    
    result.append(current_word)
    
    return result