"""
QUESTION:
Write a function `validate_nested_parens(lst)` that takes a list of two strings containing only opening and closing parentheses. The function should return 'Affirmative' if the strings can be concatenated to form a valid nested parentheses string, and 'Negative' otherwise.
"""

def validate_nested_parens(lst):
    s = ''.join(lst)
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            if count == 0:
                return 'Negative'
            count -= 1
    return 'Affirmative' if count == 0 else 'Negative'