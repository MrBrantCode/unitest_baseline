"""
QUESTION:
Write a recursive function `hi_it` that takes a string `name` as input, reverses the order of its characters, and returns the reversed string. The function should use recursion and handle the base case where the input string is empty.
"""

def hi_it(name):
    if name == "":
        return ""
    return hi_it(name[1:]) + name[0]