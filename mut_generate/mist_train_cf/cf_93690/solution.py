"""
QUESTION:
Design a function `count_occurrences` that takes a string and a list of characters as input and returns a list of the number of occurrences of each character in the string, ignoring any occurrences within double-quoted substrings. The function should not count occurrences when the character is within a substring enclosed in double quotes.
"""

def count_occurrences(string, characters):
    occurrences = []
    inside_quotes = False
    count_dict = {char: 0 for char in characters}

    for char in string:
        if char == '"':
            inside_quotes = not inside_quotes
        elif not inside_quotes and char in characters:
            count_dict[char] += 1

    return list(count_dict.values())