"""
QUESTION:
Write a function `max_balanced_parentheses` that takes a string of parentheses as input and returns the maximum number of left and right parentheses that can be balanced. The function should consider only the given expression and find the maximum balanced parentheses without adding any extra parentheses.
"""

def max_balanced_parentheses(s):
    """
    This function calculates the maximum number of balanced parentheses in a given string.

    Args:
        s (str): A string of parentheses.

    Returns:
        tuple: A tuple containing the maximum number of left and right balanced parentheses.

    """
    max_left = 0
    max_right = 0
    balance = 0
    for parenthesis in s:
        if parenthesis == '(':
            balance += 1
            max_left = max(max_left, balance)
        else:
            balance -= 1
    balance = 0
    for parenthesis in s[::-1]:
        if parenthesis == ')':
            balance += 1
            max_right = max(max_right, balance)
        else:
            balance -= 1
    return max_left, max_right