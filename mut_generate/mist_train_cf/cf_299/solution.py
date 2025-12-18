"""
QUESTION:
Design a function named `count_occurrences` that takes two arguments: a given string and a string of characters to find. The function should return a list of the number of occurrences of each character in the given string, ignoring any occurrences within double-quoted substrings and their nested counterparts.
"""

def count_occurrences(given_string, character_to_find):
    occurrences = [0] * len(character_to_find)
    inside_quotes = False
    nested_quotes = []

    for char in given_string:
        if char == '"':
            if inside_quotes:
                nested_quotes.pop()
            else:
                nested_quotes.append([])
            inside_quotes = not inside_quotes
            continue

        if not inside_quotes and char in character_to_find:
            in_nested_quotes = False
            for nested in reversed(nested_quotes):
                if char in nested:
                    in_nested_quotes = True
                    break
            if not in_nested_quotes:
                index = character_to_find.index(char)
                occurrences[index] += 1

    return occurrences