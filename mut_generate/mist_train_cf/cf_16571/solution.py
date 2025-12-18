"""
QUESTION:
Create a function named `split_string` that takes in an input string and a delimiter. The function should split the input string into a list of words separated by the delimiter, ignoring any delimiter surrounded by double quotes and treating any word enclosed in double quotes as a single entity. The function should also correctly handle nested double quotes. The function should return a list of words.
"""

def split_string(s, delimiter):
    result = []
    word = ""
    inside_quotes = False
    quote_count = 0

    for char in s:
        if char == '"':
            quote_count += 1
            inside_quotes = not inside_quotes

        if char == delimiter and not inside_quotes:
            result.append(word)
            word = ""
        else:
            word += char

    result.append(word)

    return result