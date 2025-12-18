"""
QUESTION:
Create a function called `reverse_string` that takes a string as input and returns the reversed string. The function should iterate through each character in the input string in reverse order and concatenate each character to the result string.
"""

def reverse_string(s):
    reversed_str = ""
    for char in s[::-1]:
        reversed_str += char
    return reversed_str