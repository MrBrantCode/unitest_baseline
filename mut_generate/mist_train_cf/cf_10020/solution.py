"""
QUESTION:
Create a function named `split_string` that takes two parameters: `input_string` and `delimiter`. The function should split the `input_string` into a list of words based on the `delimiter`. However, it should ignore the `delimiter` if it is surrounded by double quotes and treat any substring enclosed in double quotes as a single entity.
"""

def split_string(input_string, delimiter):
    words = []
    current_word = ""
    inside_quotes = False
    
    for char in input_string:
        if char == delimiter and not inside_quotes:
            words.append(current_word)
            current_word = ""
        elif char == '"':
            inside_quotes = not inside_quotes
        else:
            current_word += char
    
    words.append(current_word)
    
    return words