"""
QUESTION:
Implement a function `DictDiff(book1, book2)` that compares two dictionaries and returns a dictionary representing the differences between them. The keys in the dictionaries represent price levels and the values represent order quantities. The function should identify the differences in terms of both additions and subtractions, with negative values indicating subtractions.
"""

def DictDiff(book1, book2):
    diff = {}
    for key in book1:
        if key not in book2:
            diff[key] = book1[key]
        elif book1[key] != book2[key]:
            diff[key] = book1[key] - book2[key]
    for key in book2:
        if key not in book1:
            diff[key] = -book2[key]
    return diff