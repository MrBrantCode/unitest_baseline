"""
QUESTION:
Write a function named `reverse_string` to reverse a given string. The function should take a string as an input and return the reversed string. 

The function should be implemented using only basic data types and control structures. No external libraries or built-in string reversal functions should be used.
"""

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s