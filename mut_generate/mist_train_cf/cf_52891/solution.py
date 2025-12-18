"""
QUESTION:
Given a list of strings containing 'n' strings with only '(' and ')' characters, write a function `advanced_nested_parentheses(lst, n)` that checks if a combination of these strings can result in a correctly nested parentheses string with single, double, or multiple levels of nested parentheses. If possible, return 'Yes' along with the length of the maximum nested parentheses; otherwise, return 'No' and 0.
"""

def advanced_nested_parentheses(lst, n):
    max_nested = 0
    open_count = 0
    all_parentheses = ''.join(lst)
    for char in all_parentheses:
        if char == '(':
            open_count += 1
            if open_count > max_nested:
                max_nested = open_count
        if char == ')':
            if open_count == 0:
                return ('No', 0)
            open_count -= 1
    if open_count != 0:
        return ('No', 0)
    return ('Yes', max_nested)