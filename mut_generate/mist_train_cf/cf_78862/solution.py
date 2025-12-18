"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of dictionaries, removes any duplicate rows, and returns the resulting list of dictionaries. The function should not use any external libraries.
"""

def remove_duplicates(data):
    seen = set()
    result = []
    for row in data:
        row_tuple = tuple(sorted(row.items()))
        if row_tuple not in seen:
            seen.add(row_tuple)
            result.append(row)
    return result