"""
QUESTION:
Create a function `indexString` that takes two parameters: a list of strings `listStr` and a target string `s`. The function should return a new list containing all strings from `listStr` that include the target string `s`.
"""

def indexString(listStr, s):
    return [i for i in listStr if s in i]