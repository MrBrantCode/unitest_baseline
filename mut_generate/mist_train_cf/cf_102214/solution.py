"""
QUESTION:
Create a function `indexString` that takes a list of strings `listStr` and a substring `s` as input. The function should return a dictionary where the keys are the strings from `listStr` that contain the substring `s` and the values are the lengths of the corresponding strings.
"""

def indexString(listStr, s):
    return {i: len(i) for i in listStr if s in i}