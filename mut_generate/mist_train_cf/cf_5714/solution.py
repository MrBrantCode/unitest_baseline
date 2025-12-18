"""
QUESTION:
Implement a function `split_string_with_quotes` that takes two parameters: `string` and `delimiter`. The function should split the input `string` by the specified `delimiter` while ignoring any `delimiter` that appears within double quotes in the string. The function should handle cases where the double quotes are not properly closed by treating the string as if the missing closing quote was at the end of the string.
"""

def split_string_with_quotes(string, delimiter):
    output = []
    current_word = ''
    inside_quotes = False
    unclosed_quotes = False

    for char in string:
        if char == delimiter and not inside_quotes:
            if current_word:
                output.append(current_word)
            current_word = ''
        elif char == '"':
            if inside_quotes:
                current_word += char
                inside_quotes = False
            else:
                current_word += char
                inside_quotes = True
                unclosed_quotes = True
        else:
            current_word += char

    if current_word:
        output.append(current_word)

    if inside_quotes and unclosed_quotes:
        output[-1] += '"'

    return output