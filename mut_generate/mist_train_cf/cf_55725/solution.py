"""
QUESTION:
Write a function 'detectDupes' that takes a tuple as input and returns a boolean indicating whether the tuple contains duplicate entries and a set of the duplicate entries. The function should consider case sensitivity for string entries. The function should be able to handle tuples containing different data types. The function should return a boolean value of True and a set of duplicates if there are any duplicate entries in the tuple; otherwise, it should return False and an empty set.
"""

def detectDupes(input_tuple):
    seen = set()
    duplicates = set()
    for item in input_tuple:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return len(duplicates) > 0, duplicates