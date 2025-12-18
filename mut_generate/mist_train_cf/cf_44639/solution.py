"""
QUESTION:
Write a function `count_char_except_brackets(string, char)` that takes a string and a character as input, and returns the number of occurrences of the character in the string, ignoring any occurrences within parentheses or brackets.
"""

def count_char_except_brackets(string, char):
    count = 0
    ignore = False
    for c in string:
        if c in '([':
            ignore = True
        elif c in ')]':
            ignore = False
        elif not ignore and c == char:
            count += 1
    return count