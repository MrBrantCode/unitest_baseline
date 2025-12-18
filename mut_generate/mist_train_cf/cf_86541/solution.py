"""
QUESTION:
Remove all occurrences of a given substring from a string while maintaining the original order of characters, excluding instances of the substring as part of a larger word. Implement a Python function `remove_substring` that takes two parameters: the original string and the substring to be removed. Ensure the function is case-sensitive and only removes the substring if it appears as a standalone word.
"""

def remove_substring(string, substring):
    words = string.split()  
    result = []
    for word in words:
        if word != substring or not (word.endswith(substring) or word.startswith(substring)):
            result.append(word)  
    return ' '.join(result)  