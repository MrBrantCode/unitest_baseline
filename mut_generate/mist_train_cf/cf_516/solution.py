"""
QUESTION:
Write a function `count_char_outside_brackets_quotes` that takes two parameters: `string` and `char`. The function should return the number of occurrences of `char` in `string`, excluding any occurrences within parentheses `()` and curly brackets `{}`, and also excluding any occurrences within single or double quotation marks. The function should assume that the input string is well-formed, i.e., all brackets and quotation marks are properly nested and closed.
"""

def count_char_outside_brackets_quotes(string, char):
    count = 0
    is_inside_quotes = False
    parentheses_count = 0
    curly_brackets_count = 0

    for ch in string:
        if ch in ['\'', '\"']:
            is_inside_quotes = not is_inside_quotes
        elif ch == '(':
            parentheses_count += 1
        elif ch == ')':
            parentheses_count -= 1
        elif ch == '{':
            curly_brackets_count += 1
        elif ch == '}':
            curly_brackets_count -= 1
        elif ch == char and not is_inside_quotes and parentheses_count == 0 and curly_brackets_count == 0:
            count += 1

    return count