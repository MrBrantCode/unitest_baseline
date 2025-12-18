"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions. The function should use a while loop to iterate through the input string in reverse order.
"""

def reverse_string(s):
    reversed_string = ""
    index = len(s) - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1
    return reversed_string