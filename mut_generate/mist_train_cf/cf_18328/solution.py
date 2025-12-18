"""
QUESTION:
Write a function called `maxBalancedBrackets` that takes a string expression as input and returns the maximum number of balanced pairs of parentheses, curly braces, and square brackets in the expression. The function should reset the count whenever it encounters an unbalanced sequence.
"""

def maxBalancedBrackets(s: str) -> int:
    """
    This function calculates the maximum number of balanced pairs of parentheses, 
    curly braces, and square brackets in the given expression.

    Args:
        s (str): The input expression.

    Returns:
        int: The maximum number of balanced pairs of parentheses, curly braces, 
             and square brackets in the expression.
    """
    max_count = 0
    curr_count = 0
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack and stack[-1] == pairs[char]:
                stack.pop()
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                stack = []
                curr_count = 0

    return max_count