"""
QUESTION:
Write a function `match_parens` that takes a list of two strings containing parentheses and squared brackets. The function should check if the concatenation of the two strings results in a properly nested parentheses and brackets string. It should return `True` if a valid string can be formed and `False` otherwise. The function should handle empty strings and individual pairs of parentheses or brackets correctly.
"""

def match_parens(lst):
    stack = []
    bracket_map = {"(": ")", "[": "]"}
    
    for bracket in lst[0] + lst[1]:
        if bracket in bracket_map:
            stack.append(bracket)
        else:
            try:
                if bracket_map[stack.pop()] != bracket:
                    return False
            except IndexError:
                return False
    return stack == []