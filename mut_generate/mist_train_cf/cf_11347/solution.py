"""
QUESTION:
Write a function `max_balanced_parentheses` that takes a string of parentheses as input and returns the maximum number of balanced pairs of parentheses that can be formed from the given expression. The input string will only contain left and right parentheses.
"""

def max_balanced_parentheses(s):
    """
    This function calculates the maximum number of balanced pairs of parentheses 
    that can be formed from the given expression.

    Args:
    s (str): A string of parentheses.

    Returns:
    int: The maximum number of balanced pairs of parentheses.
    """
    stack = []
    max_count = 0
    current_count = 0
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
                
    max_count = max(max_count, current_count)
    return max_count