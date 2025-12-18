"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or libraries.
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string