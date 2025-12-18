"""
QUESTION:
Construct a function `remove_special_chars` that takes a string as input, removes any non-alphanumeric characters, and returns the modified string in lowercase. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def remove_special_chars(string):
    result = ""
    for char in string:
        if char.isalnum():
            result += char.lower()
    return result