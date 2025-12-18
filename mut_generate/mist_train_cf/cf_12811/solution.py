"""
QUESTION:
Write a function `split_string_with_quotes(string, delimiter)` that splits a string into substrings based on a specified delimiter, while ignoring any delimiter that appears within double quotes. The function should return a list of substrings. The string is split at the delimiter only when it is not inside double quotes.
"""

def split_string_with_quotes(string, delimiter):
    result = []
    inside_quotes = False
    current_word = ""

    for char in string:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == delimiter and not inside_quotes:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char

    result.append(current_word)
    return result