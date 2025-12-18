"""
QUESTION:
Create a function called `str_filter` that takes two arguments: a list of strings and a string. The function should return a list of booleans where each boolean value at index n represents whether the nth string in the list contains the provided string. The function should be optimized for large inputs.
"""

def str_filter(stringList, matchString):
    return [matchString in s for s in stringList]