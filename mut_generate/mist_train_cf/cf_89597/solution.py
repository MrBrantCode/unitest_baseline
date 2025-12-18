"""
QUESTION:
Create a function named `remove_special_chars` that takes a string as input, removes any non-alphanumeric characters, converts any uppercase letters to lowercase, and returns the modified string. The input string only contains printable ASCII characters, and the function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def remove_special_chars(string):
    result = ""
    for char in string:
        if char.isalnum():
            result += char.lower()
    return result