"""
QUESTION:
Design a function named `find_occurrences` that takes two arguments: `string` and `char`. The function should find and return the number of occurrences of `char` in `string`, ignoring any occurrences of `char` within substrings enclosed in double quotes.
"""

def find_occurrences(string, char):
    occurrences = 0
    inside_quotes = False

    for i in range(len(string)):
        if string[i] == '"':
            inside_quotes = not inside_quotes

        if string[i] == char and not inside_quotes:
            occurrences += 1

    return occurrences