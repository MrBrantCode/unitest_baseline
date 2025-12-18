"""
QUESTION:
Create a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods, loops, `len()`, `slice()`, `split()`, or any other built-in functions or methods that handle string manipulation.
"""

def reverse_string(string):
    if string == "":
        return ""
    else:
        return reverse_string(string[1:]) + string[0]