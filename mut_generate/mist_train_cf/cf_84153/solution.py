"""
QUESTION:
Write a function `match_parens` that takes a list of two strings, each consisting solely of open '(' or closed ')' parentheses. The function should return 'Yes' if the strings can be concatenated in either order to form a correctly nested parentheses string, and 'No' otherwise.
"""

def match_parens(lst):
    """
    This function checks if two strings of parentheses can be concatenated in either order to form a correctly nested parentheses string.

    Args:
        lst (list): A list of two strings, each consisting solely of open '(' or closed ')' parentheses.

    Returns:
        str: 'Yes' if the strings can be concatenated in either order to form a correctly nested parentheses string, 'No' otherwise.
    """
    def is_valid(parens):
        stack = []
        for p in parens:
            if p == '(':
                stack.append(p)
            elif p == ')' and stack:
                stack.pop()
            else:
                return False
        return not stack

    return 'Yes' if is_valid(lst[0] + lst[1]) or is_valid(lst[1] + lst[0]) else 'No'