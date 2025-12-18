"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods. The function should iterate over the input string in reverse order and concatenate the characters to form the reversed string.
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string