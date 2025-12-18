"""
QUESTION:
Write a function named `transform_tuples` that takes a list of tuples as input and returns a dictionary. The function should handle cases where the list contains non-unique keys by keeping the first occurrence of each key and ignoring the rest, and cases where the list contains non-tuple elements or tuples of incorrect size (not equal to 2) by ignoring them. The function should not modify the original list.
"""

def transform_tuples(list_tuples):
    result = {}
    for tup in list_tuples:
        if isinstance(tup, tuple) and len(tup) == 2:
            if tup[0] not in result:
                result[tup[0]] = tup[1]
    return result