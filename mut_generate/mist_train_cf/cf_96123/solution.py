"""
QUESTION:
Write a recursive function called `hi_it` that takes a string `name` as input and returns the characters in `name` in reverse order. The function must use recursion to solve the problem.
"""

def hi_it(name):
    if name == "":
        return ""
    return hi_it(name[1:]) + name[0]