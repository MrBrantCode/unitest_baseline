"""
QUESTION:
Remove all non-alphanumeric characters from a given string and convert it to lowercase. 

Implement a function named "remove_special_chars" that takes a non-empty string as input, removes all spaces, punctuation, and special characters, and converts all uppercase letters to lowercase. The output should contain only alphanumeric characters in lowercase, and the order of characters should remain the same as in the input string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def remove_special_chars(s):
    output = ""
    for char in s:
        if char.isalnum():
            output += char.lower()
    return output