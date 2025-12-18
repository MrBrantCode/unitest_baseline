"""
QUESTION:
Create a function named `alter_list` that takes two parameters: a list of strings and a replacement string. The function should replace the last three elements of the list with the replacement string. If the list has fewer than three elements, it should replace all elements with the replacement string.
"""

def alter_list(words, replacement):
    if len(words) < 3:
        return [replacement] * len(words)
    else:
        words[-3:] = [replacement] * 3
        return words