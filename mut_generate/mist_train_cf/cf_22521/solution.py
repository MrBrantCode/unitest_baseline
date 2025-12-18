"""
QUESTION:
Write a function named `count_o_outside_quotes` that takes a string `s` as input and returns the number of times the letter "o" appears in the string, excluding any occurrences within quotation marks.
"""

def count_o_outside_quotes(s):
    count = 0
    in_quote = False
    for char in s:
        if char == '"':
            in_quote = not in_quote
        elif char.lower() == 'o' and not in_quote:
            count += 1
    return count