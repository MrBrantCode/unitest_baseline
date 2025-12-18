"""
QUESTION:
Write a function `extract_items` that takes a tuple as input and returns a new tuple containing the 3rd and 4th last items from the input tuple. The function should not convert the tuple into another data structure and should work with tuples of any length (as long as the length is at least 4).
"""

def extract_items(tuple):
    return tuple[-4:-2]