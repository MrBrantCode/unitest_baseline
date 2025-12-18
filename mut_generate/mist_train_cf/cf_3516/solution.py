"""
QUESTION:
Write a function `max_balanced_brackets` that calculates the maximum number of balanced left and right parentheses, curly braces, and square brackets in a given expression. The expression may contain angle brackets and double quotes in addition to the brackets, but these will not be considered when calculating the maximum number of balanced brackets.
"""

def max_balanced_brackets(s):
    """
    Calculate the maximum number of balanced left and right parentheses, curly braces, and square brackets in a given expression.

    Args:
        s (str): The input expression.

    Returns:
        int: The maximum number of balanced brackets.
    """

    # Create a dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Create a set of opening brackets for easy lookup
    open_brackets = set(['(', '{', '['])
    
    # Initialize a stack to keep track of the opening brackets
    stack = []
    
    # Initialize a counter for the maximum number of balanced brackets
    max_balanced = 0
    
    # Iterate over each character in the expression
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in open_brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_map:
            # If the stack is not empty and the top of the stack matches the current closing bracket
            if stack and stack[-1] == bracket_map[char]:
                # Pop the opening bracket from the stack and increment the max_balanced counter
                stack.pop()
                max_balanced += 1
    
    # Return the maximum number of balanced brackets
    return max_balanced