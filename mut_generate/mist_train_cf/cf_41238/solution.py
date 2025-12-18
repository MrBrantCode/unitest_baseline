"""
QUESTION:
Implement a function `countLonelyClosingBraces` that takes a string as input and returns the count of closing curly braces (`}`) that are not preceded by any opening curly brace (`{`).
"""

def count_lonely_closing_braces(input_string):
    lonely_count = 0
    open_brace = False
    for char in input_string:
        if char == '{':
            open_brace = True
        elif char == '}':
            if not open_brace:
                lonely_count += 1
            else:
                open_brace = False
    return lonely_count