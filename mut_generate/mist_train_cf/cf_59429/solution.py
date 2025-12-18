"""
QUESTION:
Create a function `truncate_string(string)` that truncates a given string to display only the first 4 unique characters. If the string has less than 4 unique characters, return the string with all unique characters in sorted order.
"""

def truncate_string(string):
    unique_chars = []
    for ch in string:
        if ch not in unique_chars:
            unique_chars.append(ch)
        if len(unique_chars) == 4:
            break
    if len(unique_chars) == 4:
        return ''.join(unique_chars)
    else:
        return ''.join(sorted(unique_chars))