"""
QUESTION:
Write a function `split_string_with_quotes` that takes two parameters: a string and a delimiter. The function should split the string into substrings using the delimiter, but ignore the delimiter if it appears within double quotes in the string.
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