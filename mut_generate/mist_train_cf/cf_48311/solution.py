"""
QUESTION:
Given a list of strings where each string consists only of open parentheses '(' or close parentheses ')', write a function match_parens that checks if it is possible to concatenate the strings in some order, such that the resulting string will have properly nested parentheses. The function should return 'Yes' if a properly nested string can be achieved, and return 'No' otherwise.
"""

def match_parens(lst):
    open_count = 0
    close_count = 0

    for string in lst:
        for char in string:
            if char == "(":
                open_count += 1
            else:
                close_count += 1

    if open_count != close_count:
        return "No"

    unclosed = 0
    for string in lst:
        for char in string:
            if char == "(":
                unclosed += 1
            else:
                unclosed -= 1
            if unclosed < 0:
                return "No"
    return "Yes"