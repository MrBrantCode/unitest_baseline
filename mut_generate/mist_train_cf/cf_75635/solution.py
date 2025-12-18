"""
QUESTION:
Write a function `matchParens` that takes two strings as input, each containing only open '(' or close ')' parentheses. The function should determine if it's possible to concatenate these two strings in some order to result in a balanced string, where all parentheses are matched, and the first character of the final string is not ')' and the last character is not '('. The function should return 'Yes' if a balanced string is possible, and 'No' otherwise.
"""

def matchParens(first, last):
    """
    Determine if it's possible to concatenate two strings of parentheses in some order to result in a balanced string.

    Args:
        first (str): The first string of parentheses.
        last (str): The second string of parentheses.

    Returns:
        str: 'Yes' if a balanced string is possible, 'No' otherwise.
    """
    open_count = first.count('(') + last.count('(')
    close_count = first.count(')') + last.count(')')

    if open_count == close_count and first[0] != ')' and last[-1] != '(':
        return 'Yes'
    elif open_count == close_count and first[0] != ')' and first[-1] != '(' and last[0] != ')':
        return 'Yes'
    else:
        return 'No'