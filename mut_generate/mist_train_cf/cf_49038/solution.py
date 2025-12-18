"""
QUESTION:
Write a function named `alphabeticOrder` that takes two parameters: a list of strings and an optional string parameter for sort order. The function should sort the list of strings in either ascending or descending alphabetical order based on the sort order parameter, which defaults to 'asc'. The function should ignore strings containing non-alphabetic characters or empty strings and return a new sorted list. The function should also handle invalid sort order inputs by printing an error message and returning None.
"""

def alphabeticOrder(words, order='asc'):
    cleanWords = [word for word in words if word.isalpha() and word != '']
    if order == 'asc':
        return sorted(cleanWords)
    elif order == 'desc':
        return sorted(cleanWords, reverse=True)
    else:
        print("Invalid sort order. Please choose 'asc' for ascending or 'desc' for descending")
        return None