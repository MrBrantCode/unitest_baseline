"""
QUESTION:
Create a function named `reverse_string` that takes a string as input and returns the reversed string with all white spaces removed. The function should be case-sensitive, handle special characters, and have a time complexity of O(n).
"""

def reverse_string(string):
    reversed_string = ""
    for char in string[::-1]:
        if char != ' ':
            reversed_string += char
    return reversed_string