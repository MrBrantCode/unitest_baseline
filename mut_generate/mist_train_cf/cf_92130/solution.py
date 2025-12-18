"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in string manipulation functions or libraries. The function should iterate through the characters in the input string in reverse order and return the resulting reversed string.
"""

def entance(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string